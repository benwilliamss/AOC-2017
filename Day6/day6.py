def string_list_to_int_list(string_list):
    """
    converts string to int and updates this value in the list

    """
    for index in range(0 ,len(string_list)):
        string_list[index] = int(string_list[index])




def cycle_count(memory_bank_list):

    configurations_of_memory = {} #map to store memory bank configs
    no_repeat_configurations = True
    cycle_count = 0

    

    while no_repeat_configurations:
         
        memory_bank_tuple = tuple(memory_bank_list)
        #print_tuple(memory_bank_tuple)
        
        #adds the tuple: cycle count 
        #or returns the value of the previous cycle_count if it already exists
        suspected_cycle_count = configurations_of_memory.setdefault(memory_bank_tuple, cycle_count)
        
        if suspected_cycle_count != cycle_count:
            print("cycle count till repeat", cycle_count)
            #repeat occurence 
            print("cycles between repeats:",cycle_count-suspected_cycle_count)
            no_repeat_configurations = False
        
        else:

                       
            max_value = max(memory_bank_list) #amount distributed
            
            max_value_index = memory_bank_list.index(max_value) 
            #needed for index to start at & reset index
            memory_bank_list[max_value_index] = 0 #resets to 0 
            
            index_count = max_value_index + 1
            while max_value:
                #upto the sixteeth value - prevent index out of range
                if index_count == 16:
                     index_count =0#wraparound
                
                #take away from max, add one to next index
                max_value -=1
                memory_bank_list[index_count] +=1
                index_count +=1
            

            cycle_count +=1 #redistribute cycles 
            
            
            
            
            





                

            
            

    #check if it exits in the 
    #find max
    


with open("input.txt","r") as f:
    string_of_txt = f.read()
    memory_bank_list = string_of_txt.split()
    
    string_list_to_int_list(memory_bank_list)#parse string list to int list

    cycle_count(memory_bank_list) #counts redistribute cycles till repeats configs


   
    


