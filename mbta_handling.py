import pandas as pd
from Research_Framework.ResearchHandler import ResearchHandler


def blank(df: pd.DataFrame) -> pd.DataFrame:
    return df


def get_combined_df(nodespath: str, gsepath: str, travel_timepath: str) -> pd.DataFrame:
    nodesfp = "data/mbta_rapid_transit/MBTA_NODE.shp"
    gsefp = "data/GSE.csv"
    travel_timesfp = "data/TravelTimes_2026/2026-02_HRTravelTimes.csv"

    nodes = ResearchHandler(
        source=nodesfp, shapefile=True, handling_function=mbta_init, initialize=True
    )
    gse = ResearchHandler(source=gsefp, handling_function=mbta_init, initialize=True)
    travel_times = ResearchHandler(
        source=travel_timesfp, handling_function=mbta_init, initialize=True
    )


def mbta_init(input_df: pd.DataFrame) -> pd.DataFrame:
    output_df = input_df.copy()
    return output_df
