TelAPI Web SDK Examples
=======================

In this simple tutorial we will go through few simple example scenarios for using TelAPI's web SDK:

* [Example 1](#example-1) - use web client to call TelAPI servers which will respond with a "hello world" message
* [Example 2](#example-2) - use web client to call another web client
* [Example 3](#example-3) - use web client to call a landline
* [Example 4](#example-4) - call web client from a landline
* [Example 5](#example-5) - simple conferencing tool (static)
* [Example 6](#example-6) - simple conferencing tool (dynamic with Flask; only one conference at the time)
* [Example 7](#example-7) - use web client to call a landline letting user choose which number he will call (dynamic with Flask)
* [Example 8](#example-8) - simple conferencing tool (dynamic with Flask; multiple conferences at the time)

To try any of the examples, you must first register on [TelAPI](http://www.telapi.com). After that, create an application by clicking Numbers -> Manage Applications -> Add Application. Fill in a friendly name for your application and you can start testing the examples.

## Example 1 ##

1. Set your application voice URL to this URL: `https://raw.githubusercontent.com/tpiha/telapi-webrtc-examples/master/example1/inbound.xml` (you can also use your own from the example1/inbound.xml if it's accessible from the Internet)
2. Run [cURL 1](#curl-1)
3. Copy sid from cURL result to index.html, variable token
4. Copy client_password from cURL result to index.html, variable password
5. Open example1/index.html in your browser (testing on local web server or uploaded on the Internet)

## Example 2 ##

1. Set your application voice URL to this URL: `https://raw.githubusercontent.com/tpiha/telapi-webrtc-examples/master/example2/inbound.xml` (you can also use your own from the example2/inbound.xml if it's accessible from the Internet)
2. Run [cURL 2a](#curl-2)
3. Copy sid from cURL result to callee.html, variable token
4. Copy client_password from cURL result to callee.html, variable password
5. Run [cURL 2b](#curl-2)
6. Copy sid from cURL result to caller.html, variable token
7. Copy client_password from cURL result to caller.html, variable password
8. Open example2/callee.html in your browser (testing on local web server or uploaded on the Internet)
9. Open example2/caller.html in your browser (testing on local web server or uploaded on the Internet)
10. Make a call and answer it

## Example 3 ##

1. Edit example3/inbound.xml, put desired phone number instead of [PhoneNumber], save and upload to the location accessible from the internet
2. Set your application voice URL to your inbound.xml URL
3. Run [cURL 3](#curl-3)
4. Copy sid from cURL result to index.html, variable token
5. Copy client_password from cURL result to index.html, variable password
6. Open example3/index.html in your browser (testing on local web server or uploaded on the Internet)
7. Make a call

## Example 4 ##

1. Set your application voice URL to this URL: `https://raw.githubusercontent.com/tpiha/telapi-webrtc-examples/master/example4/inbound.xml` (you can also use your own from the example4/inbound.xml if it's accessible from the Internet)
2. Run [cURL 4](#curl-4)
3. Copy sid from cURL result to index.html, variable token
4. Copy client_password from cURL result to index.html, variable password
5. Purchase a number on TelAPI by clicking Numbers -> Buy A Phone Number
6. Check "Use application voice settings" checkbox on application settings page, choose your application and click Save
7. Open example4/index.html in your browser (testing on local web server or uploaded on the Internet)
8. Call purchased number from your phone and answer the call in browser

## Example 5 ##

1. Set your application voice URL to this URL: `https://raw.githubusercontent.com/tpiha/telapi-webrtc-examples/master/example5/inbound.xml` (you can also use your own from the example5/inbound.xml if it's accessible from the Internet)
2. Run [cURL 5a](#curl-5)
3. Copy sid from cURL result to participant1.html, variable token
4. Copy client_password from cURL result to participant1.html, variable password
5. Run [cURL 5b](#curl-5)
6. Copy sid from cURL result to participant2.html, variable token
7. Copy client_password from cURL result to participant2.html, variable password
8. Open example5/participant1.html in your browser (testing on local web server or uploaded on the Internet)
9. Open example5/participant2.html in your browser (testing on local web server or uploaded on the Internet)
10. Dial a conference from both of them

## Example 6 ##

This is our first dynamic example and we are using Flask (Python) for it and ngrok to access it from the Internet.

To prepare, set your application voice URL to this one: `https://raw.githubusercontent.com/tpiha/telapi-webrtc-examples/master/example6/inbound.xml` (you can also use your own from the example6/inbound.xml if it's accessible from the Internet).

To install the example (on Linux), go to example6 folder and run this in bash:

```
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
./conference.py
```

Now start ngrok in another tab:

```
ngrok 5000
```

and you can start opening the URL from the ngrok output and dialing into the conference.

## Example 7 ##

In our second dynamic example and we are also using Flask (Python) and ngrok to access it from the Internet. To install (on Linux), go to example7 folder and run this in bash:

```
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
./dialer.py
```

Now start ngrok in another tab:

```
ngrok 5000
```

and you can open the URL from the ngrok output and dial your phone number.

**Notice -** you must also setup your application voice URL to your ngrok output URL appended with 'xml'. For example: https://4eae35b5.ngrok.com/xml

## Example 8 ##

In our last dynamic example and we are also using Flask (Python) and ngrok to access it from the Internet. To install (on Linux), go to example8 folder and run this in bash:

```
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
./conference.py
```

Now start ngrok in another tab:

```
ngrok 5000
```

and you can open the URL from the ngrok output, create a new conference and send link to the other participants to dial in.

**Notice -** you must also setup your application voice URL to your ngrok output URL appended with 'xml'. For example: https://4eae35b5.ngrok.com/xml

## cURL shell lines for the examples ##

#### cURL 1 ####

`cURL -X POST 'https://api.telapi.com/v1/Accounts/[AccountSid]/Applications/[ApplicationSid]/Clients/Tokens.json' -u '[AccountSid]:[AccountToken]' -d 'Nickname=test'`

#### cURL 2 ####

`cURL -X POST 'https://api.telapi.com/v1/Accounts/[AccountSid]/Applications/[ApplicationSid]/Clients/Tokens.json' -u '[AccountSid]:[AccountToken]' -d 'Nickname=callee'`

`cURL -X POST 'https://api.telapi.com/v1/Accounts/[AccountSid]/Applications/[ApplicationSid]/Clients/Tokens.json' -u '[AccountSid]:[AccountToken]' -d 'Nickname=caller'`

#### cURL 3 ####

`cURL -X POST 'https://api.telapi.com/v1/Accounts/[AccountSid]/Applications/[ApplicationSid]/Clients/Tokens.json' -u '[AccountSid]:[AccountToken]' -d 'Nickname=test'`

#### cURL 4 ####

`cURL -X POST 'https://api.telapi.com/v1/Accounts/[AccountSid]/Applications/[ApplicationSid]/Clients/Tokens.json' -u '[AccountSid]:[AccountToken]' -d 'Nickname=callee'`

#### cURL 5 ####

`cURL -X POST 'https://api.telapi.com/v1/Accounts/[AccountSid]/Applications/[ApplicationSid]/Clients/Tokens.json' -u '[AccountSid]:[AccountToken]' -d 'Nickname=participant1'`

`cURL -X POST 'https://api.telapi.com/v1/Accounts/[AccountSid]/Applications/[ApplicationSid]/Clients/Tokens.json' -u '[AccountSid]:[AccountToken]' -d 'Nickname=participant2'`
