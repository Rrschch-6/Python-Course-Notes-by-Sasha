
from tkinter import*
root=Tk()
root.title('My Window')

text=Text(root)
text.pack(side='left',fill=Y)
text.config(width=20,height=30)

sc=Scrollbar(root,command=text.yview)
sc.pack(side='right',fill='y')

text.config(yscrollcommand=sc.set)

text.tag_add('line1','1.0','1.8')
text.tag_config('line1',background='red',foreground='blue')

text.config(state='disable')
text.config(cursor='spider')

#"arrow"
#"circle"
#"clock"
#"cross"
#"dotbox"
#"exchange"
#"fleur"
#"heart"
#"man"
#"mouse"
#"pirate"
#"plus"
#"shuttle"
#"sizing"
#"spider"
#"spraycan"
#"star"
#"target"
#"tcross"
#"trek"
#"watch"




