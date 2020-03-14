
/*

user name:  bethanybeachbum
API_ID:  
a960790f

API_KEY:
399046c67a2d31b9d2b1b67f7492e7de

THIS WORKS AT A TERMINAL: 
curl -H "Content-Type:application/json" -H "x-app-id: a960790f" -H "x-app-key: 399046c67a2d31b9d2b1b67f7492e7de" -X POST -d '{"query":"butter"}' https://trackapi.nutritionix.com/v2/natural/nutrients

GET to get the resource
PUT to update  or stores content at a resource
POST to Insert
DELETE to delete
*/

Natural Language Request for Food Logging
This endpoint requires an app ID and app key from https://developer.nutritionix.com/admin/access_details

/* FIRST REQUEST EXAMPLE */

POST https://trackapi.nutritionix.com/v2/natural/nutrients

HEADERS Content-Type:application/json, x-app-id:NutritionixAppID, x-app-key:NutritionixAppKey

BODY:

{
 "query":"for breakfast i ate 2 eggs, bacon, and french toast",
 "timezone": "US/Eastern"
}

/* SECON REQUEST */
Request
POST /v2/natural/nutrients

{
 "query":"1 cup chicken noodle soup"
}
Response:

{
    "foods": [
        {
            "food_name": "chicken noodle soup",
            "brand_name": null,
            "serving_qty": 1,
            // AND A WHOLE LOT MORE