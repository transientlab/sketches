from graph_tool.all import *
import re

power_net = Graph(directed=True)
line_name = power_net.new_vp("string")
line_cable = power_net.new_ep("float")
power_net.vertex_properties["name"] = line_name
power_net.edge_properties["cable"] = line_cable

lines = []
with open('dzialka', 'r') as instal:
    for line in instal:
        if '---' in line:
            break
        if line.startswith('#'):
            pass
        else:
            splitline = line.split(':')
            splitline = [i.strip() for i in splitline]
            if '' in splitline:
                pass
            else:
                lines.append(splitline)

depth = 0
parents, children, v_info = [], [], []
for idx, line in enumerate(lines):
    print(line)
    if '{' in line:
        parents.append(power_net.add_vertex())
        line_name[parents[depth]] = str(line[1])
        depth += 1
    elif '}' in line:
        depth -= 1
        if depth > 0 :
            e = power_net.add_edge(parents[-2], parents[-1])
            line_cable[e] = str(parents[depth-1])
            parents.pop()
        else:
            e = power_net.add_edge(parents[0], parents[1])
        
        
    else:
        child = power_net.add_vertex()
        line_name[child] = str(line[1])
        e = power_net.add_edge(parents[depth-1], child)
        line_cable[e] = str(line[0])


# depth = 0
# parents, children, v_info = [], [], []
# for idx, line in enumerate(lines):
#     if '{' in line:
#         depth += 1
#         parents.append(power_net.add_vertex())
#         line_name[parents[depth-1]] = str(line[0])
#     elif '}' in line:
#         # print(parents[0], depth-1)
#         for child in children:
#             power_net.add_edge(parents[depth-1], child)
            

#         depth -= 1
#         if depth > 0:
#             power_net.add_edge(parents[-2], parents[-1])
#         parents.pop()
#         children = []
        
#     else:
#         children.append(power_net.add_vertex())
#         line_name[children[-1]] = str(line[0])

pos = radial_tree_layout(power_net, 0)
graph_draw(power_net, pos, edge_pen_width=line_cable, vertex_text=power_net.vertex_properties["name"], vertex_font_size=10, output_size=(500, 500))
