Type of cryptographic commitment that is homomorphic with respect to addition. This means that the sum of two commitments can be verified without revealing the individual values.

Formally, if:
$$
C_1\ =\ commit(m_1,\ r_1) \quad C_2\ =\ commit(m_2,\ r_2)
$$

then:
$$
C_3\ =\ C_1 \cdot C_2\ =\ commit(m_1\ +\ m_2,\ r_1\ +\ r_2)
$$

This property becomes useful, for example, to conceal the amounts of tokens exchanged in cryptocurrency systems, such as RGB, while still being able to verify the totals.
