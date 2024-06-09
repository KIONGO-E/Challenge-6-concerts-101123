from classes.many_to_many import Band
from classes.many_to_many import Concert
from classes.many_to_many import Venue

class TestConcert:
    """Concert in many_to_many.py"""
    
    def test_has_date(self):
        """Concert is initialized with a date"""
        band = Band(name="boygenius", hometown="NYC")
        venue = Venue(name="Theatre", city="NYC")
        concert = Concert(date="Nov 5", band=band, venue=venue)

        assert concert.date == "Nov 5"

    def test_date_is_mutable_string(self):
        """dates are mutable strings"""
        band = Band(name="boygenius", hometown="NYC")
        venue = Venue(name="Theatre", city="NYC")
        concert = Concert(date="Nov 5", band=band, venue=venue)

        concert.date = "Nov 15"
        assert isinstance(concert.date, str)
        assert concert.date == "Nov 15"

        # comment out the next two lines if using Exceptions
        concert.date = 15
        assert concert.date == "Nov 15"

        # uncomment the next two lines if using Exceptions
        # with pytest.raises(Exception):
        #     concert.date = 15

    def test_date_has_length(self):
        """dates are longer than 0 characters"""
        band = Band(name="boygenius", hometown="NYC")
        venue = Venue(name="Theatre", city="NYC")
        concert = Concert(date="Nov 5", band=band, venue=venue)

        assert len(concert.date) > 0

        # comment out the next two lines if using Exceptions
        concert.date = ""
        assert concert.date == "Nov 5"

        # uncomment the next two lines if using Exceptions
        # with pytest.raises(Exception):
        #     concert.date = ""

    def test_has_venue(self):
        """Concert is initialized with a venue"""
        band = Band(name="boygenius", hometown="NYC")
        venue = Venue(name="Theatre", city="NYC")
        concert = Concert(date="Nov 5", band=band, venue=venue)

        assert concert.venue == venue

    def test_venue_of_type_venue(self):
        """venue is of type Venue"""
        band = Band(name="boygenius", hometown="NYC")
        venue = Venue(name="Theatre", city="NYC")
        concert = Concert(date="Nov 5", band=band, venue=venue)

        # comment out the next two lines if using Exceptions
        concert.venue = "My house"
        assert concert.venue.name == "Theatre"

        assert isinstance(concert.venue, Venue)

        # uncomment the next two lines if using Exceptions
        # with pytest.raises(Exception):
        #     concert.venue = "My house"

    def test_venue_is_mutable(self):
        """venue is mutable"""
        band = Band(name="boygenius", hometown="NYC")
        venue_1 = Venue(name="Theatre", city="NYC")
        venue_2 = Venue(name="House Extended", city="LA")
        concert = Concert(date="Nov 5", band=band, venue=venue_1)

        concert.venue = venue_2
        assert concert.venue.name == "House Extended"
        assert isinstance(concert.venue, Venue)

    def test_has_band(self):
        """Concert is initialized with a band"""
        band = Band(name="boygenius", hometown="NYC")
        venue = Venue(name="Theatre", city="NYC")
        concert = Concert(date="Nov 5", band=band, venue=venue)

        assert concert.band == band

    def test_band_of_type_band(self):
        """concert's band is of type Band"""
        band = Band(name="boygenius", hometown="NYC")
        venue = Venue(name="Theatre", city="NYC")
        concert = Concert(date="Nov 5", band=band, venue=venue)

        # comment out the next two lines if using Exceptions
        concert.band = "My friends"
        assert concert.band.name == "boygenius"

        assert isinstance(concert.band, Band)

        # uncomment the next two lines if using Exceptions
        # with pytest.raises(Exception):
        #     concert.band = "My friends"

    def test_band_is_mutable(self):
        """concert's band is mutable"""
        band_1 = Band(name="boygenius", hometown="NYC")
        band_2 = Band(name="girlgenius", hometown="Boston")
        venue_1 = Venue(name="Theatre", city="NYC")
        concert = Concert(date="Nov 5", band=band_1, venue=venue_1)

        concert.band = band_2
        assert concert.band.name == "girlgenius
