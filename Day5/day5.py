def steps_to_exit_maze_offset_1(list_of_lines):
    
    #going to use indexing of the list to act as the respective steps

    still_in_maze = True
    
    total_steps= len(list_of_lines)-1 #starts from 0 indexing
    step_count = 0

    current_step_index = 0 #starting point
    
    while still_in_maze:
        current_step_value = int(list_of_lines[current_step_index]) #value to move forward/backwards    
        
        steps_taken = current_step_value + current_step_index #movement taken from current position
        step_count+=1 

        if steps_taken > total_steps:
            #exited the maze
            print("step count is", step_count)
            still_in_maze = False

        else:
            #still in maze
            
            #incrememnt and change current position value
            list_of_lines[current_step_index] =  current_step_value + 1 
            #update position
            current_step_index = steps_taken





def  steps_to_exit_maze_offset_3(list_of_lines):
    still_in_maze = True
    
    total_steps= len(list_of_lines)-1 #starts from 0 indexing
    step_count = 0

    current_step_index = 0 #starting point
    
    while still_in_maze:

        current_step_value = int(list_of_lines[current_step_index]) #value to move forward/backwards   
                

        steps_taken = current_step_value + current_step_index #movement taken from current position
        step_count+=1 

        if steps_taken > total_steps:
            #exited the maze
            print("step count with a 3 or more offset:", step_count) 
            still_in_maze = False

        else:
            #still in maze

            #If the value to move forward by is 3 or more decrement 
            #else increment the value at the index by 1
            if current_step_value >= 3:
                
                list_of_lines[current_step_index] =  current_step_value - 1
                
            else:
                list_of_lines[current_step_index] =  current_step_value + 1
            
            #update position
            current_step_index = steps_taken




with open("input.txt","r") as f:
    list_of_lines = f.readlines()
    list_of_lines_copy = list_of_lines.copy()
   
    steps_to_exit_maze_offset_1(list_of_lines)
    steps_to_exit_maze_offset_3(list_of_lines_copy)

    

