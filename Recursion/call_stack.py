# Building own call stack

def sum_to_one(n):
    result = 1
    call_stack = []
    
    while n != 1:
        execution_context = {"n_value": n}
        call_stack.append(execution_context)
        n -= 1
    print("BASE CASE REACHED")
    print(call_stack)

    while call_stack:
        return_value = call_stack.pop()
        result += return_value["n_value"]
        print(f"Adding {return_value['n_value']} to {result}")

    return result, call_stack

print(sum_to_one(4)[0])