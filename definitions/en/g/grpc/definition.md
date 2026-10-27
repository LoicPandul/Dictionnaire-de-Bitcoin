Remote Procedure Call framework developed by Google. gRPC uses the Protocol Buffers format to serialize data and the HTTP/2 protocol for transport, providing fast, typed communication between a client and a server.

In the Lightning ecosystem, gRPC is the main interface LND uses to expose its features. Tools such as LNCLI interact with the Lightning node through gRPC calls to manage channels, send payments, check balances, or configure routing.
