class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None
    
    def add_child(self, child):
        child.parent = self
        self.children.append(child)
        
    def get_level(self):
        level = 0
        p = self.parent
        while(p):
            level += 1
            p = p.parent
        return level
        
    def print_tree(self):
        spaces = ' ' * self.get_level() * 4
        prefix = spaces + "|__" if self.parent else ""
        print(prefix,self.data)
        if(self.children):
            for child in self.children:
                child.print_tree()

def build_tree():
    root = TreeNode("Electronics")
    
    laptop = TreeNode("Laptop")
    laptop.add_child(TreeNode("Mac"))
    laptop.add_child(TreeNode("Lenovo"))
    laptop.add_child(TreeNode("Dell"))
    
    cellphone = TreeNode("CellPhone")
    cellphone.add_child(TreeNode("iPhone"))
    cellphone.add_child(TreeNode("Vivo"))
    cellphone.add_child(TreeNode("Xiaomi"))
    
    tv = TreeNode("TV")
    tv.add_child(TreeNode("LG"))
    tv.add_child(TreeNode("Samgsung"))
    tv.add_child(TreeNode("Philips"))

    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)

    return root

if __name__ == '__main__':
    root = build_tree()
    root.print_tree()