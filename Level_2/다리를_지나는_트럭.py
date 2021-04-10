def solution(bridge_length, weight, truck_weights):
    bridge = [0]*bridge_length
    time = 0
    total_weights = 0
    
    while truck_weights:
        total_weights -= bridge[0]
        bridge.pop(0)
        
        if total_weights + truck_weights[0] <= weight:
            total_weights += truck_weights[0]
            bridge.append(truck_weights.pop(0))
        else :
            bridge.append(0)
        
        time += 1
        
    return time + bridge_length