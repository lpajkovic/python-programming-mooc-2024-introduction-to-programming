# Write your solution here
def search_by_name(filename:str, word:str)->list:
    
    recipes=return_recipe_name(filename)
    ret_recipes=[]
    for recipe, recipe_data in recipes.items():
        if word.lower() in recipe.lower():
            ret_recipes.append(recipe)
            
    return ret_recipes
 
def search_by_time(filename:str, prep_time:str)->list:
    
    recipes=return_recipe_name(filename)
    ret_recipes={}
    
    for recipe, recipe_data in recipes.items():
        for data in recipe_data:
            if isinstance(data,int):
                if data<=prep_time:
                    ret_recipes[recipe]=data
    ret_output=[]
    for recipe, prep in ret_recipes.items():
        ret_output.append(f"{recipe}, preparation time {prep} min")
    
    return ret_output
       
def search_by_ingredient(filename:str, ingredient:str)->list:
    
    recipes=return_recipe_name(filename)
    ret_recipes=[]
    ret_data={}
    for recipe, recipe_data in recipes.items():
        if ingredient in recipe_data:
            ret_recipes.append(recipe)
    
    for recipe, recipe_data in recipes.items():
        if recipe in ret_recipes:
            for data in recipe_data:
                if isinstance(data,int):
                    ret_data[recipe]=data
                    
    ret_output=[]
    for recipe, prep in ret_data.items():
        ret_output.append(f"{recipe}, preparation time {prep} min")
    
    return ret_output
          

def return_recipe_name(filename:str)->dict:
    
    recipes=[]
    ret_recipes=[]
    recipe_dict={}
    with open(filename) as recipe_list:
        
        for line in recipe_list:
            line=line.replace("\n","")
            recipes.append(line)
        recipes.append("")
          
        for i in range(0,len(recipes)):
            if i==0 or recipes[i-1]=="":
                ret_recipes.append(recipes[i])
                recipe_data=[]
                j=i+1
                while True:
                    if j>len(recipes):
                        break
                    if recipes[j]=="":
                        break
                    if recipes[j].isdigit():
                        recipes[j]=int(recipes[j])
                    recipe_data.append(recipes[j])
                    j=j+1
                recipe_dict[recipes[i]]=recipe_data
    return recipe_dict

if __name__=="__main__":
    print(search_by_name("recipes1.txt", "cake"))
    print(search_by_time("recipes1.txt", 20))
    print(search_by_ingredient("recipes1.txt", "eggs"))