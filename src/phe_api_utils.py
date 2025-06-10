import requests
import pandas as pd
import time

# Base URL for Fingertips API
BASE_URL = "https://fingertips.phe.org.uk/api/"

def fetch_json(endpoint: str, params: dict = None):
    """
    Helper to GET JSON from a Fingertips API endpoint and return the parsed object.
    Automatically raises for HTTP errors and includes a polite pause.
    """
    url = BASE_URL.rstrip('/') + endpoint
    try:
        resp = requests.get(url, params=params)
        resp.raise_for_status()
        time.sleep(0.2)  # Polite pause to not overwhelm the API
        return resp.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None

def get_profiles() -> pd.DataFrame:
    """Fetch a DataFrame of all available Profiles."""
    data = fetch_json('/profiles')
    return pd.DataFrame(data) if data else pd.DataFrame()

def get_profile_indicators(profile_id: int) -> pd.DataFrame:
    """Fetch all indicator metadata for a given profile."""
    data = fetch_json(f'/indicator_metadata/by_profile_id', params={'profile_id': profile_id})
    if not data:
        return pd.DataFrame()
    df = pd.DataFrame.from_dict(data, orient='index')
    df.index.name = 'IndicatorID'
    return df

def get_area_types() -> pd.DataFrame:
    """Fetch a DataFrame of all Area Types."""
    data = fetch_json('/area_types')
    return pd.DataFrame(data) if data else pd.DataFrame()

def get_areas_for_type(area_type_id: int) -> pd.DataFrame:
    """Fetch all areas under a specific AreaTypeID."""
    data = fetch_json(f'/area_types/{area_type_id}/areas')
    return pd.DataFrame(data) if data else pd.DataFrame()

def get_data_for_indicator(indicator_id: int, area_type_id: int, parent_area_code: str = None) -> pd.DataFrame:
    """
    Fetch time series data for a given Indicator and AreaType.
    Optionally filters by a parent area code (e.g., an ICB or region).
    """
    params = {
        'indicator_id': indicator_id,
        'area_type_id': area_type_id
    }
    if parent_area_code:
        params['parent_area_code'] = parent_area_code

    data = fetch_json('/all_data/for_indicator_at_area_type', params=params)
    return pd.DataFrame(data) if data else pd.DataFrame()