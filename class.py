class TrafficSite:
    """
    A class representing a car park site.

    Attributes:
        site_id (int): The unique identifier for the car park site.
        name (str): The name of the car park site.
        capacity (int): The maximum capacity of the car park site.
        current_count (int): The current number of vehicles parked at the site.
    """

    def __init__(self, site_id, name, capacity):
        """Initialize the TrafficSite instance with provided details."""
        self.site_id = site_id
        self.name = name
        self.capacity = capacity
        self.current_count = 0

    def update_count(self, diff):
        """
        Update the current vehicle count at the car park site.

        Args:
            diff (int): The difference in the vehicle count (positive for entry, negative for exit).
        """
        self.current_count += diff

    def get_occupancy_rate(self):
        """
        Calculate and return the occupancy rate of the car park site.

        Returns:
            float: The occupancy rate as a percentage.
        """
        return self.current_count / self.capacity if self.capacity != 0 else 0.0

    def get_historical_data(self):
        """
        Retrieve historical data for the car park site.

        Returns:
            list: A list of historical data points for analysis.
        """
        # Implementation for historical data retrieval
        pass


class TrafficManagement:
    """
    A class representing the traffic management system.

    Attributes:
        sites (list): A list of TrafficSite instances managed by the system.
    """

    def __init__(self):
        """Initialize the TrafficManagement system."""
        self.sites = []

    def add_site(self, site):
        """
        Add a new car park site to the traffic management system.

        Args:
            site (TrafficSite): The TrafficSite instance to be added.
        """
        self.sites.append(site)

    def remove_site(self, site_id):
        """
        Remove a car park site from the traffic management system based on site_id.

        Args:
            site_id (int): The site_id of the car park site to be removed.
        """
        self.sites = [site for site in self.sites if site.site_id != site_id]

    def get_site_by_id(self, site_id):
        """
        Get a car park site from the traffic management system based on site_id.

        Args:
            site_id (int): The site_id of the car park site to be retrieved.

        Returns:
            TrafficSite or None: The corresponding TrafficSite instance if found, else None.
        """
        for site in self.sites:
            if site.site_id == site_id:
                return site
        return None
