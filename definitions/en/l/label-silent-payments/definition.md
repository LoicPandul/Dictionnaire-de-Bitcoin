Integer used in the Silent Payments protocol to modify the initial static address and create many other static addresses. Labels make it possible to separate payments received through Silent Payments by using a different static address for each purpose, without adding too much operational burden to the detection of these payments (scanning). Bob uses a static address $B$, made up of two public keys: $B_{scan}$ for scanning and $B_{spend}$ for spending. The hash of $b_{scan}$ and an integer $m$, multiplied by the generator point $G$, is added to the spend public key $B_{spend}$ to create a sort of new spend public key $B_m$:
$$B_m\ =\ B_{spend}\ +\ hash(b_{scan}\ \Vert\ m) \cdot G$$

For example, the first key $B_1$ is obtained this way:
$$B_1\ =\ B_{spend}\ +\ hash(b_{scan}\ \Vert\ 1) \cdot G$$

The static address published by Bob is now made up of $B_{scan}$ and $B_m$. For example, the first static address, with label $1$, is:
$$B\ =\ B_{scan}\ \Vert\ B_1$$

Labels start at $1$ because label $0$ is reserved for change. Alice, who wants to send bitcoin to the labeled static address provided by Bob, derives the one-time payment address $P_0$ using the new $B_1$ in place of $B_{spend}$:
$$P_0\ =\ B_1\ +\ hash(inputHash \cdot a \cdot B_{scan}\ \Vert\ 0) \cdot G$$

In fact, Alice does not even need to know that Bob has a labeled address: she simply uses the second part of the static address he gave her, which here is the value $B_1$ rather than $B_{spend}$. To scan for payments, Bob always uses the value of his initial static address with $B_{spend}$, as follows:
$$P_0\ =\ B_{spend}\ +\ hash(inputHash \cdot b_{scan} \cdot A\ \Vert\ 0) \cdot G$$

He then subtracts the value he finds for $P_0$ from each output, one by one. Next, he checks whether one of the results of these subtractions matches the value of one of the labels used in his wallet. If there is a match, for example for output #4 with label $1$, that output is a Silent Payment associated with his labeled static address $B_1$:
$$Out_4\ -\ P_0\ =\ hash(b_{scan}\ \Vert\ 1) \cdot G$$

This works because:
$$B_1\ =\ B_{spend}\ +\ hash(b_{scan}\ \Vert\ 1) \cdot G$$

With this method, Bob can use a multitude of static addresses (with $B_1$, $B_2$, $B_3$...), all derived from his base static address ($B\ =\ B_{scan}\ \Vert\ B_{spend}$), to keep his purposes clearly separated.

Note, however, that this separation of static addresses only helps with personal wallet management and does not separate identities. Since they all share the same $B_{scan}$, it is very easy to link all the static addresses together and conclude that they belong to a single entity.
