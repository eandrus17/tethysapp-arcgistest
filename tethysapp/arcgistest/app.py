from tethys_sdk.base import TethysAppBase, url_map_maker


class Arcgistest(TethysAppBase):
    """
    Tethys app class for ArcGISTest.
    """

    name = 'ArcGISTest'
    index = 'arcgistest:home'
    icon = 'arcgistest/images/icon.gif'
    package = 'arcgistest'
    root_url = 'arcgistest'
    color = '#27ae60'
    description = 'This is an app developed by Emily Andrus that tests some of the functionality of ArcGIS JavaScript.'
    tags = ''
    enable_feedback = False
    feedback_emails = []

    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (
            UrlMap(
                name='home',
                url='arcgistest',
                controller='arcgistest.controllers.home'
            ),

           UrlMap(
                name='interdensity',
                url='arcgistest/interdensity',
                controller='arcgistest.controllers.interdensity'
            ),
        )

        return url_maps
