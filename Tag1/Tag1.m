fid = fopen("Tag1_daten.txt");
C = textscan(fid, '%d', 'MultipleDelimsAsOne',true, 'Delimiter','\n', 'HeaderLines',0);
data = C{1};

%%
sum((data(2:end)-data(1:end-1))>0)


%%
last_sum = sum(data(1:3));
greater = 0;

for i = 2:length(data)-2
    current_sum = sum(data(i:i+2));
    if current_sum > last_sum
        greater = greater + 1;
    end
    last_sum = current_sum;
end

greater