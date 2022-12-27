from pydantic import BaseModel, validator
from bridge.config import BridgeConfig



class ReviewsRequest(BaseModel):
    config: BridgeConfig
    # skip: int
    # select: str 
    # unselect: str 
    top: int
    # orderby: str

    @validator('top')
    def top_must_be_in_range(cls, value: int):
        if not isinstance(value, int):
            raise ValueError(f"number must be an int. Gave {type(value)}")
    
        if not 0 < value < 201:
            raise ValueError("number must be '0 < number < 201'")
        
        return value

    @property
    def base_api_url(self) -> str:
        return "https://api.bridgedataoutput.com/api/v2/OData"

    @property
    def reviews_url(self) -> str:
        return f"{self.base_api_url}/reviews/Reviews"

    @property
    def base_url(self) -> str:
        return f"{self.reviews_url}?access_token={self.config.server_token}"


    
    def query(self) -> str:
        """ Query for pulling reviews data

        Returns:
            str: https://api.bridgedataoutput.com/api/v2/OData/reviews/Reviews?access_token=ihklhdsfgkjhkjhdfg&$top=200
        """
        return f"{self.base_url}&$top={self.top}"
   
