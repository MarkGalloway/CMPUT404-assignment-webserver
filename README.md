### TODO
-----------------------------------------------------------------  
X - Pass Unit Tests  
  
According to http://www.jmarshall.com/easy/http/#http1.1servers a HTTP 1.1 complient server needs:  
_ - require the Host: header from HTTP 1.1 clients  
_ - accept absolute URL's in a request  
_ - accept requests with chunked data  
_ - either support persistent connections, or include the "Connection: close" header with each response  
_ - use the "100 Continue" response appropriately  
X - include the Date: header in each response  
_ - handle requests with If-Modified-Since: or If-Unmodified-Since: headers  
_ - support at least the GET and HEAD methods  
_ - support HTTP 1.0 requests  



### Contributors / Licensing
-----------------------------------------------------------------  

Generally everything is LICENSE'D under the Apache 2 license by Abram Hindle.

server.py contains contributions from:

* Abram Hindle  
* Eddie Antonio Santos  
* Tamara Bain  
* Mark Galloway  
But the server.py example is derived from the python documentation
examples thus some of the code is Copyright © 2001-2013 Python
Software Foundation; All Rights Reserved under the PSF license (GPL
compatible) http://docs.python.org/2/library/socketserver.html

### References
-----------------------------------------------------------------  
   
**Hypertext Transfer Protocol Status Code Definitions -- HTTP/1.1**   
URL: http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html

**HTTP 1.1 Servers**
URL: http://www.jmarshall.com/easy/http/#http1.1servers
