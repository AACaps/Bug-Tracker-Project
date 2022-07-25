from flask import Blueprint
from Tracker.helpers import Apology

errors = Blueprint('errors', __name__)

@errors.app_errorhandler(400)
def error_400(error):
    return Apology(code=error,title="Bad Request", message="The server cannot or will not process the request due to something that is perceived to be a client error (e.g., malformed request syntax, invalid request message framing, or deceptive request routing."), 400

"""
Client error responses

400 Bad Request

    The server cannot or will not process the request due to something that is perceived to be a client error (e.g., malformed request syntax, invalid request message framing, or deceptive request routing).
401 Unauthorized

    Although the HTTP standard specifies "unauthorized", semantically this response means "unauthenticated". That is, the client must authenticate itself to get the requested response.
402 Payment Required Experimental

    This response code is reserved for future use. The initial aim for creating this code was using it for digital payment systems, however this status code is used very rarely and no standard convention exists.
403 Forbidden

    The client does not have access rights to the content; that is, it is unauthorized, so the server is refusing to give the requested resource. Unlike 401 Unauthorized, the client's identity is known to the server.
404 Not Found

    The server can not find the requested resource. In the browser, this means the URL is not recognized. In an API, this can also mean that the endpoint is valid but the resource itself does not exist. Servers may also send this response instead of 403 Forbidden to hide the existence of a resource from an unauthorized client. This response code is probably the most well known due to its frequent occurrence on the web.
405 Method Not Allowed

    The request method is known by the server but is not supported by the target resource. For example, an API may not allow calling DELETE to remove a resource.
406 Not Acceptable

    This response is sent when the web server, after performing server-driven content negotiation, doesn't find any content that conforms to the criteria given by the user agent.
407 Proxy Authentication Required

    This is similar to 401 Unauthorized but authentication is needed to be done by a proxy.
408 Request Timeout

    This response is sent on an idle connection by some servers, even without any previous request by the client. It means that the server would like to shut down this unused connection. This response is used much more since some browsers, like Chrome, Firefox 27+, or IE9, use HTTP pre-connection mechanisms to speed up surfing. Also note that some servers merely shut down the connection without sending this message.
409 Conflict

    This response is sent when a request conflicts with the current state of the server.
410 Gone

    This response is sent when the requested content has been permanently deleted from server, with no forwarding address. Clients are expected to remove their caches and links to the resource. The HTTP specification intends this status code to be used for "limited-time, promotional services". APIs should not feel compelled to indicate resources that have been deleted with this status code.
411 Length Required

    Server rejected the request because the Content-Length header field is not defined and the server requires it.
412 Precondition Failed

    The client has indicated preconditions in its headers which the server does not meet.
413 Payload Too Large

    Request entity is larger than limits defined by server. The server might close the connection or return an Retry-After header field.
414 URI Too Long

    The URI requested by the client is longer than the server is willing to interpret.
415 Unsupported Media Type

    The media format of the requested data is not supported by the server, so the server is rejecting the request.
416 Range Not Satisfiable

    The range specified by the Range header field in the request cannot be fulfilled. It's possible that the range is outside the size of the target URI's data.
417 Expectation Failed

    This response code means the expectation indicated by the Expect request header field cannot be met by the server.
418 I'm a teapot

    The server refuses the attempt to brew coffee with a teapot.
421 Misdirected Request

    The request was directed at a server that is not able to produce a response. This can be sent by a server that is not configured to produce responses for the combination of scheme and authority that are included in the request URI.
422 Unprocessable Entity (WebDAV)

    The request was well-formed but was unable to be followed due to semantic errors.
423 Locked (WebDAV)

    The resource that is being accessed is locked.
424 Failed Dependency (WebDAV)

    The request failed due to failure of a previous request.
425 Too Early Experimental

    Indicates that the server is unwilling to risk processing a request that might be replayed.
426 Upgrade Required

    The server refuses to perform the request using the current protocol but might be willing to do so after the client upgrades to a different protocol. The server sends an Upgrade header in a 426 response to indicate the required protocol(s).
428 Precondition Required

    The origin server requires the request to be conditional. This response is intended to prevent the 'lost update' problem, where a client GETs a resource's state, modifies it and PUTs it back to the server, when meanwhile a third party has modified the state on the server, leading to a conflict.
429 Too Many Requests

    The user has sent too many requests in a given amount of time ("rate limiting").
431 Request Header Fields Too Large

    The server is unwilling to process the request because its header fields are too large. The request may be resubmitted after reducing the size of the request header fields.
451 Unavailable For Legal Reasons

    The user agent requested a resource that cannot legally be provided, such as a web page censored by a government.

Server error responses

500 Internal Server Error

    The server has encountered a situation it does not know how to handle.
501 Not Implemented

    The request method is not supported by the server and cannot be handled. The only methods that servers are required to support (and therefore that must not return this code) are GET and HEAD.
502 Bad Gateway

    This error response means that the server, while working as a gateway to get a response needed to handle the request, got an invalid response.
503 Service Unavailable

    The server is not ready to handle the request. Common causes are a server that is down for maintenance or that is overloaded. Note that together with this response, a user-friendly page explaining the problem should be sent. This response should be used for temporary conditions and the Retry-After HTTP header should, if possible, contain the estimated time before the recovery of the service. The webmaster must also take care about the caching-related headers that are sent along with this response, as these temporary condition responses should usually not be cached.
504 Gateway Timeout

    This error response is given when the server is acting as a gateway and cannot get a response in time.
505 HTTP Version Not Supported

    The HTTP version used in the request is not supported by the server.
506 Variant Also Negotiates

    The server has an internal configuration error: the chosen variant resource is configured to engage in transparent content negotiation itself, and is therefore not a proper end point in the negotiation process.
507 Insufficient Storage (WebDAV)

    The method could not be performed on the resource because the server is unable to store the representation needed to successfully complete the request.
508 Loop Detected (WebDAV)

    The server detected an infinite loop while processing the request.
510 Not Extended

    Further extensions to the request are required for the server to fulfill it.
511 Network Authentication Required

    Indicates that the client needs to authenticate to gain network access.

"""