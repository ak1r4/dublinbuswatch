from dublinbuswatch.api import RTPI


def find_bus_location(stopid, routeid):
    upcoming_routes = RTPI.rt_bus_info(stopid, routeid)
    results = upcoming_routes['results']
    if not results:
        return None

    previous_stops = get_previous_stops(stopid, routeid)
    previous_stops.reverse()

    bus_loc_time = [
        [(r['duetime'], r['arrivaldatetime']) for r in results]
    ]

    for stop in previous_stops:
        routes = RTPI.rt_bus_info(stop['stopid'], routeid)['results']
        if not routes:
            break
        if len(routes) < len(results):
            routes = [None] * (len(results) - len(routes)) + routes

        bus_loc_time.append([
            [(r['duetime'], r['arrivaldatetime'])] if r else []
            for r in routes
        ])

    return bus_loc_time


def get_previous_stops(stopid, routeid):
    route_stops = RTPI.route_info(routeid, 'bac')['results']

    for direction in route_stops:
        previous_stops = []
        for stop in direction['stops']:
            if stop['stopid'] == stopid:
                return previous_stops
            else:
                previous_stops.append(stop)
    return []
