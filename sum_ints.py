
# def minimumTime(numOfParts, parts):
#     if numOfParts >= 2:
#         parts.sort()
#         t = parts.pop(0) + parts.pop(0)
#         parts = [t] + parts
#         return minimumTime(numOfParts - 1, parts) + t
#     return parts.pop(0)


# parts = [1,2,5,10,35,89]
# nparts = 6
# print(minimumTime(nparts, parts))

def optimalUtilization(maxTravelDist, forwardRouteList, returnRouteList):
    routes_combinations = []
    optimal_routes = []
    best_coverage = 0
    for fr in forwardRouteList:
        for rr in returnRouteList:
            routes_combinations.append([fr[0], rr[0], fr[1] + rr[1]])
    for rc in routes_combinations:
        if rc[2] <= maxTravelDist and rc[2] >= best_coverage:
            best_coverage = rc[2]
            optimal_routes.append(rc.pop())
    return optimal_routes

