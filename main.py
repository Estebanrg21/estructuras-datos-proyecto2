import btree

d= btree.Tree(btree.Node("deportes","deportes",1))

d.insert_question("futbolista","Campbell")
d.insert_question("futbolista","keylor navas")
d.insert_question("futbolista","bryan ruiz" )
d.insert_question("futbolista","Celso Borges")
d.insert_question("exentrenador","pinto")
d.insert_question("jugador de la liga","moreira",d.get("futbolista"))
d.insert_question("jugador del twente","ugalde",d.get("futbolista"))
d.print()
print("\n\n\n\n\n\n")
d.interchange_nodes(d.get("jugador de la liga"),d.get("futbolista"))
d.print()
#print(d.get_parent_of_node("futbolista")[1].key)
