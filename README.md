# dbitnkr196723
DBT1303PythonProject
# Import necessary libraries and modules

class TrafficSite:
    # Constructor to initialize the site details
    def __init__(self, site_id, name, capacity):
        self.site_id = site_id
        self.name = name
        self.capacity = capacity
        self.current_count = 0

    # Method to update the current vehicle count
    def update_count(self, diff):
        self.current_count += diff

    # Method to calculate and return the occupancy rate
    def get_occupancy_rate(self):
        return self.current_count / self.capacity if self.capacity != 0 else 0.0

    # Method to retrieve historical data for analysis
    def get_historical_data(self):
        # Implementation for historical data retrieval
        pass

class TrafficManagement:
    # Constructor to initialize the traffic management system
    def __init__(self):
        self.sites = []

    # Method to add a new site to the system
    def add_site(self, site):
        self.sites.append(site)

    # Method to remove a site from the system based on site_id
    def remove_site(self, site_id):
        self.sites = [site for site in self.sites if site.site_id != site_id]

    # Method to get a site based on site_id
    def get_site_by_id(self, site_id):
        for site in self.sites:
            if site.site_id == site_id:
                return site
        return None
