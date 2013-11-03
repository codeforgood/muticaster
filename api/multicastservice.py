__author__ = 'sravi'

relays_dict = {
    "S": {"name": "Small", "throughput": 1, "cost": 0.01, "subnet": "10.0.1.0/24"},
    "M": {"name": "Medium", "throughput": 5, "cost": 0.05, "subnet": "10.0.2.0/24"},
    "L": {"name": "Large", "throughput": 10, "cost": 0.10, "subnet": "10.0.3.0/24"},
    "X": {"name": "Super", "throughput": 25, "cost": 0.25, "subnet": "10.0.4.0/24"}
}
relay_types = ["X", "L", "M", "S"]


def get_host_ip_of_type(relay_type, instance):
    return relays_dict[relay_type]["subnet"].rpartition('.')[0] + "." + str(instance)


def get_routing(recipients):
    recipients_count = len(recipients)
    rt = {}
    for i in range(len(relay_types)):
        if recipients_count == 0:
            break
        relay_hosts_needed = recipients_count / relays_dict[relay_types[i]]["throughput"]
        recipients_count = recipients_count % relays_dict[relay_types[i]]["throughput"]
        rt[relay_types[i]] = relay_hosts_needed
    return rt


def get_recipients_assigned_for_routing(routing_table, recipients):
    routes = []
    start = 0
    for i in range(len(relay_types)):
        hosts_needed = routing_table[relay_types[i]]
        if hosts_needed > 0:
            for j in range(hosts_needed):
                host_ip = get_host_ip_of_type(relay_types[i], j+1)
                end = start + relays_dict[relay_types[i]]["throughput"]
                route = {'ip': host_ip, 'recipients': recipients[start: end]}
                start = end
                routes.append(route)
    return routes

if __name__ == "__main__":
    test_recipients = ["2017061186", "5512086867", "9833961586", "2017061187", "2017061188", "20170611869",
                        "2017061186", "5512086867", "9833961586", "2017061187", "2017061188", "20170611869",
                        "2017061186", "5512086867", "9833961586", "2017061187", "2017061188", "20170611869", "2017061186",
                        "5512086867", "9833961586", "2017061187", "2017061188", "20170611869", "2017061186", "5512086867",
                        "9833961586", "2017061187", "2017061188", "20170611869", "2017061186", "5512086867", "9833961586",
                        "2017061187", "2017061188", "20170611869", "2017061186", "5512086867", "9833961586", "2017061187",
                        "2017061188", "20170611869", "2017061186", "5512086867", "9833961586", "2017061187", "2017061188",
                        "20170611869", "2017061186", "5512086867", "9833961586", "2017061187", "2017061188", "20170611869",
                        "2017061186", "5512086867", "9833961586", "2017061187", "2017061188", "20170611869", "2017061186",
                        "5512086867", "9833961586", "2017061187", "2017061188", "20170611869", "2017061186", "5512086867",
                        "9833961586", "2017061187", "2017061188", "20170611869","2017061186", "5512086867", "9833961586",
                        "2017061187", "2017061188", "20170611869","2017061186", "5512086867", "9833961586", "2017061187",
                        "2017061188", "20170611869","2017061186", "5512086867", "9833961586", "2017061187", "2017061188",
                        "20170611869","2017061186", "5512086867", "9833961586", "2017061187", "2017061188", "20170611869",
                        "2017061186", "5512086867", "9833961586", "2017061187", "2017061188", "20170611869","2017061186",
                        "5512086867", "9833961586", "2017061187", "2017061188", "20170611869","2017061186", "5512086867",
                        "9833961586", "2017061187", "2017061188", "20170611869"]
    test_routing_table = get_routing(test_recipients)
    recipients_routing = get_recipients_assigned_for_routing(test_routing_table, test_recipients)
    print test_routing_table
    print recipients_routing
