const request = require('request');

request('https://trackapi.nutritionix.com/v2/natural/nutrients', function (error, response, body) {
  
    if(!error && response.statusCode == 200){
        const parsedData = JSON.parse(body);
        console.log('$ {parsedData.name} lives in ${parsedData.city}');
        } 
});

// ROOT API:

/*
https://trackapi.nutritionix.com/



https://trackapi.nutritionix.com/v2/search/instant?query=apple?x-app-id=a960790f&x-app-id=399046c67a2d31b9d2b1b67f7492e7de

axios.get( https://trackapi.nutritionix.com/v2/search/instant?query=apple%60`, {
headers: {
"x-app-id": "a960790f",
"x-app-key":"399046c67a2d31b9d2b1b67f7492e7de"
}`


/*
const request = require('request');
request('https://trackapi.nutritionix.com/v2/natural/nutrients&appId=a960790f&appKey=399046c67a2d31b9d2b1b67f7492e7de', function (error, response, body) {
    if(!error && response.statusCode == 200){
        console.log(body);
        var parsedData = JSON.parse(body);
        console.log(parsedData);
        } 
});
*/