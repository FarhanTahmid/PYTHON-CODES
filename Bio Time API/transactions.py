import requests
import datetime
import json
from typing import Dict, List, Optional, Union


class BiotimeAPI:
    """
    Client for interacting with ZKBio Time 9.0 API to retrieve attendance data.
    
    This class handles authentication and provides methods to fetch employee
    and attendance data with various filtering options.
    """
    
    def __init__(self, server_ip: str, server_port: str, username: str, password: str):
        """
        Initialize the Biotime API client.
        
        Args:
            server_ip: The IP address of the ZKBio Time server
            server_port: The port number of the ZKBio Time server
            username: Username for API authentication
            password: Password for API authentication
        """
        self.base_url = f"http://{server_ip}"
        self.username = username
        self.password = password
        self.token = None
        self.headers = {"Content-Type": "application/json"}
    
    def authenticate(self) -> bool:
        """
        Authenticate with the ZKBio Time API and retrieve an auth token.
        
        Returns:
            bool: True if authentication was successful, False otherwise
        """
        auth_url = f"{self.base_url}/api-token-auth/"
        payload = {
            "username": self.username,
            "password": self.password
        }
        
        try:
            response = requests.post(auth_url, json=payload, headers=self.headers)
            response.raise_for_status()
            
            data = response.json()
            self.token = data.get("token")
            
            if self.token:
                self.headers["Authorization"] = f"Token {self.token}"
                return True
            return False
            
        except requests.exceptions.RequestException as e:
            print(f"Authentication error: {e}")
            return False
    
    def get_employee_by_code(self, emp_code: str) -> Dict:
        """
        Retrieve employee information by employee code.
        
        Args:
            emp_code: The employee code to search for
            
        Returns:
            Dict: Employee information or empty dict if not found
        """
        if not self.token:
            if not self.authenticate():
                return {}
        
        employee_url = f"{self.base_url}/personnel/api/employees/?emp_code={emp_code}"
        
        try:
            response = requests.get(employee_url, headers=self.headers)
            response.raise_for_status()
            
            data = response.json()
            if data.get("count", 0) > 0 and data.get("data"):
                return data["data"][0]
            return {}
            
        except requests.exceptions.RequestException as e:
            print(f"Error fetching employee: {e}")
            return {}
    
    def get_attendance_records(
        self, 
        emp_code: Optional[str] = None, 
        start_date: Optional[str] = None, 
        end_date: Optional[str] = None,
        page: int = 1,
        limit: int = 100
    ) -> List[Dict]:
        """
        Retrieve attendance records with optional filtering.
        
        Args:
            emp_code: Optional employee code to filter by
            start_date: Optional start date in format 'YYYY-MM-DD HH:MM:SS'
            end_date: Optional end date in format 'YYYY-MM-DD HH:MM:SS'
            page: Page number for pagination
            limit: Number of records per page
            
        Returns:
            List[Dict]: List of attendance records
        """
        if not self.token:
            if not self.authenticate():
                return []
        
        attendance_url = f"{self.base_url}/iclock/api/transactions/"
        params = {"page": page, "limit": limit}
        
        if emp_code:
            params["emp_code"] = emp_code
        
        if start_date:
            params["start_time"] = start_date
        
        if end_date:
            params["end_time"] = end_date
        
        try:
            response = requests.get(attendance_url, headers=self.headers, params=params)
            response.raise_for_status()
            
            data = response.json()
            return data.get("data", [])
            
        except requests.exceptions.RequestException as e:
            print(f"Error fetching attendance records: {e}")
            return []
    
    def get_daily_attendance_report(self, date: str, all_employees: bool = False) -> Dict[str, List[Dict]]:
        """
        Generate a daily attendance report for the specified date.
        
        Args:
            date: Date in 'YYYY-MM-DD' format
            all_employees: Whether to include all employees or only those with attendance records
            
        Returns:
            Dict[str, List[Dict]]: Dictionary with employee codes as keys and their attendance records as values
        """
        start_time = f"{date} 00:00:00"
        end_time = f"{date} 23:59:59"
        
        # Get all attendance records for the day
        attendance_records = self.get_attendance_records(
            start_date=start_time,
            end_date=end_time,
            limit=1000  # Adjust limit as needed to fetch all records
        )
        
        # Group records by employee
        employee_records = {}
        for record in attendance_records:
            emp_code = record.get("emp_code")
            if emp_code:
                if emp_code not in employee_records:
                    employee_records[emp_code] = []
                employee_records[emp_code].append(record)
        
        return employee_records
    
    def get_employee_attendance_report(
        self, 
        emp_code: str, 
        start_date: Optional[str] = None, 
        end_date: Optional[str] = None
    ) -> Dict:
        """
        Generate an attendance report for a specific employee.
        
        Args:
            emp_code: Employee code
            start_date: Optional start date in format 'YYYY-MM-DD'
            end_date: Optional end date in format 'YYYY-MM-DD'
            
        Returns:
            Dict: Report containing employee info and attendance records
        """
        # Get employee information
        employee = self.get_employee_by_code(emp_code)
        
        if not employee:
            return {"error": "Employee not found"}
        
        # Prepare date parameters
        start_time = f"{start_date} 00:00:00" if start_date else None
        end_time = f"{end_date} 23:59:59" if end_date else None
        
        # Get attendance records
        attendance_records = self.get_attendance_records(
            emp_code=emp_code,
            start_date=start_time,
            end_date=end_time,
            limit=1000  # Adjust limit as needed to fetch all records
        )
        
        # Organize records by date
        records_by_date = {}
        for record in attendance_records:
            punch_time = record.get("punch_time", "")
            if punch_time:
                date = punch_time.split(" ")[0]  # Extract date part
                if date not in records_by_date:
                    records_by_date[date] = []
                records_by_date[date].append(record)
        
        return {
            "employee": employee,
            "attendance": records_by_date
        }

    def get_all_attendance_records_batch(
        self, 
        start_date: Optional[str] = None, 
        end_date: Optional[str] = None,
        batch_size: int = 1000
    ) -> List[Dict]:
        """
        Retrieve all attendance records in batches to handle large datasets.
        
        Args:
            start_date: Optional start date in format 'YYYY-MM-DD'
            end_date: Optional end date in format 'YYYY-MM-DD'
            batch_size: Number of records to fetch in each batch
            
        Returns:
            List[Dict]: Complete list of attendance records
        """
        if not self.token:
            if not self.authenticate():
                return []
        
        start_time = f"{start_date} 00:00:00" if start_date else None
        end_time = f"{end_date} 23:59:59" if end_date else None
        
        all_records = []
        page = 1
        has_more = True
        
        while has_more:
            attendance_url = f"{self.base_url}/iclock/api/transactions/"
            params = {"page": page, "limit": batch_size}
            
            if start_time:
                params["start_time"] = start_time
            
            if end_time:
                params["end_time"] = end_time
            
            try:
                response = requests.get(attendance_url, headers=self.headers, params=params)
                response.raise_for_status()
                
                data = response.json()
                records = data.get("data", [])
                all_records.extend(records)
                
                # Check if there are more pages
                if data.get("next") is None:
                    has_more = False
                else:
                    page += 1
                    
            except requests.exceptions.RequestException as e:
                print(f"Error fetching batch of attendance records: {e}")
                has_more = False
        
        return all_records


# Example usage
def main():
    # Initialize the API client
    api = BiotimeAPI(
        server_ip="49.0.44.36",
        server_port="",
        username="admin",
        password="Tcl@time"
    )
    
    # Authenticate
    if not api.authenticate():
        print("Failed to authenticate with the Biotime API")
        return
    
    # Example 1: Get a specific employee
    employee = api.get_employee_by_code("10095")
    print(f"Employee: {json.dumps(employee, indent=2)}")
    
    # Example 2: Get attendance records for today
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    daily_report = api.get_daily_attendance_report(today)
    print(f"Daily attendance report: {json.dumps(daily_report, indent=2)}")
    
    # Example 3: Get attendance report for a specific employee
    start_date = (datetime.datetime.now() - datetime.timedelta(days=30)).strftime("%Y-%m-%d")
    end_date = datetime.datetime.now().strftime("%Y-%m-%d")
    employee_report = api.get_employee_attendance_report("1", start_date, end_date)
    print(f"Employee attendance report: {json.dumps(employee_report, indent=2)}")
    
    # Example 4: Get all attendance records for a date range in batches
    all_records = api.get_all_attendance_records_batch(start_date, end_date)
    print(f"Total records: {len(all_records)}")


if __name__ == "__main__":
    main()