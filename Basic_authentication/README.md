Bassic Auth
or basics access authentification
uses Username:Password to authorize client to server to keep the rest api stateless.
this is the most basic form of authentification.
it DOES NOT protect against anything but it does encode your username:password into a usable ascii character readable by HTTTP using Base64. This hides behind the Http in the Header as a very soft layer of protection. 
It is not encoded for protection, it is soley encoded to make it http formatable. 