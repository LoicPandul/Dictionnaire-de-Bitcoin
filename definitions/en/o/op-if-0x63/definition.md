Executes the following portion of the script if the value at the top of the stack is nonzero (true). If the value is zero (false), these operations are skipped, and execution jumps directly to those after `OP_ELSE`, if present. `OP_IF` starts a conditional control structure in a script. It determines the control flow of a script based on a condition supplied when the transaction is executed. `OP_IF` is used with `OP_ELSE` and `OP_ENDIF` as follows:

```text
<condition>
OP_IF
<operations if the condition is true>
OP_ELSE
<operations if the condition is false>
OP_ENDIF
```
