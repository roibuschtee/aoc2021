fopen("Tag5_daten.txt");
input = textscan(fid, '%d,%d -> %d,%d');
input = cell2mat(input);

fclose(fid);
%%

max_dim = max(input(:));
min_dim = min(input(:));
%%
area = zeros(max_dim-min_dim+1, max_dim-min_dim+1);

for i = 1:size(input,1)
   if input(i,1) == input(i,3) || input(i,2) == input(i,4)
       start_x = min(input(i,1)-min_dim+1,input(i,3)-min_dim+1);
       end_x = max(input(i,1)-min_dim+1,input(i,3)-min_dim+1);
       start_y = min(input(i,2)-min_dim+1,input(i,4)-min_dim+1);
       end_y = max(input(i,2)-min_dim+1,input(i,4)-min_dim+1);
       area(start_x:end_x, start_y:end_y) = area(start_x:end_x, start_y:end_y)+1;
   end
    
end

area = area';

sum(area>=2,'all')

%%
area = zeros(max_dim-min_dim+1, max_dim-min_dim+1);

for i = 1:size(input,1)
   if input(i,1) == input(i,3) || input(i,2) == input(i,4)
       start_x = min(input(i,1)-min_dim+1,input(i,3)-min_dim+1);
       end_x = max(input(i,1)-min_dim+1,input(i,3)-min_dim+1);
       start_y = min(input(i,2)-min_dim+1,input(i,4)-min_dim+1);
       end_y = max(input(i,2)-min_dim+1,input(i,4)-min_dim+1);
       area(start_x:end_x, start_y:end_y) = area(start_x:end_x, start_y:end_y)+1;
   else
       counter_j = 0;
       for j = input(i,1):(-1)^(input(i,1)>=input(i,3)):input(i,3)
           counter_j = counter_j +1;
           counter_k = 0;
           for k = input(i,2):(-1)^(input(i,2)>=input(i,4)):input(i,4)
               counter_k = counter_k +1;
               if counter_j == counter_k
                   area(j-min_dim+1,k-min_dim+1) = area(j-min_dim+1,k-min_dim+1)+1;
               end
           end
       end
   end
    
end

area = area';

sum(area>=2,'all')