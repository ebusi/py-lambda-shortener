# Python AWS Lambda Shortener


Quick working test for an AWS Lambda shortener. 

 - Map the urls in the `urls.json` file with the "key" and the "url" parameters, others field are not used yet;
 - Set a GET proxy endpoint in the Api Gateway;
 - Release the API
 - go to `https://{API_GW_ID}.execute-api.{REGION}.amazonaws.com/{STAGE}/g` and get redirect to google.com.