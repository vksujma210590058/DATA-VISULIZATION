#!/usr/bin/env python
# coding: utf-8

# In[3]:


# import read
# read.file_reading()
# df=read.df


# In[24]:


# import matplotlib.pyplot as plt
# import seaborn as sns
# print(unique_counts)
# print(unique_counts.index)
# min_unique_value = unique_counts.min()
# print(unique_counts[unique_counts<=10])
# print(unique_counts.dtype)
# Find columns that have the minimum unique value count
# min_unique_columns = unique_counts[unique_counts == min_unique_value].index

# unique_counts = df.nunique()
# col_star =list(unique_counts[unique_counts<=10].index)  # Choose the last column among multiple columns with the same minimum count
# # else:
# you_want=input("you want to see ")
# if you_want=="yes":
    
#     for i in col_star:
#         plt.figure(figsize=(10,10))

#         plt.subplot(2,2,1)

#         print(i)

#         # here  can write and the code
#         sns.histplot(x=df[i])
#         plt.xticks(rotation=90)
#         plt.subplot(2,2,2)
#         plt.pie(x=df[i].value_counts(),labels=df[i].value_counts().index,autopct="%1.0f%%")
#         plt.show()
# else:
#     print("okey")
#         # here  can write and the code
#     #     col_name_min = min_unique_columns[0]  
#     # print(col_star)


# In[30]:


#!/usr/bin/env python
# coding: utf-8

# In[2]:


def run_code():
    def mysql1(function):
        import pandas as pd
    #     import read
        from IPython.display import display, Image, HTML

    #  Displaying an image
    # display(Image(filename='example.png'))

    # # Displaying HTML content
    # html_#content = "<h1>Hello, World!</h1>"
    # display(HTML(html_content))


    #     file=input()
    #     import matplot.pyplot as plt
        function=f'''{function}'''
        split_list= function.split(" ")
        result_list = [item for sublist in split_list for item in sublist.split('\n')]
        final_list=[]
        for i in result_list:
            if i!="":
                final_list.append(i)
        a=final_list
        c_list=["select","from","where","groupby","having","limit"]

        j=0
        b=[]
        while j<=len(c_list)-1:
            if  c_list[j] in a:
                b.append(c_list[j])
            j=j+1





        dic={}

        try:
            for i,value in  enumerate (b):
                j=[]
                if i==len(b)-1:
                    p=a.index(value)+1

                    while p<=len(a)-1:
                        j.append(a[p])
                        p=p+1
                    dic[b[i]]=j

                elif b[i] in a:
                    p=a.index(value)+1
                    while p<=a.index(b[i+1])-1:
                        j.append(a[p])
                        p=p+1
                    dic[b[i]]=j

        except:

            print("its ok ")
    #     print(dic)

    #     keys=list(dic.keys())

        condition=''

        agg=''
        gr=''
        groupby_agg=''
        dfs=dic['from'][0]
        not_group_by=''
        if "groupby" not in list(dic.keys()) and "*" not in dic["select"]:
            not_group_by=dic["select"]
    #         print(not_group_by)
            not_group_by="["+str(not_group_by)+"]"
    #         print(not_group_by)
        if "where" in list(dic.keys()):
    #         print(eval(dfs))
            cond=dic["where"][0] 
            d=dic["where"][1] + str(dic["where"][2])
            condition='['+dfs+'.'+  cond + d+"]"
    #         print(eval(condition))
        if "groupby" in list(dic.keys()):


            agg_col={}
            groupby_col=[]
            for i in dic["groupby"]:



                i=i.replace(")","")
                if "(" in i:


                    split=list(i.split("("))
    #                 print(split)
                    if split[1] not in agg_col:


                        agg_col[split[1]]=[split[0]]

    #                     print(agg_col)
                    else: 
    #                     print(agg_col)
                        agg_col[split[1]].append(split[0])
    #                     print(agg_col)
                else:

                    groupby_col.append(i)
                    print(groupby_col)
    #         print(groupby_col)
    #         print(agg_col)
            agg=".agg(agg_col)"
            gr=".groupby(groupby_col)"
            groupby_agg=gr+agg

        if "groupby" in b:
            global q
            q=dfs+condition+groupby_agg
    #         q1=q
            q=q+".reset_index()"
        else:
            q=dfs+condition+not_group_by
    #     print(q)
    #     print(q)
        grouped_df=eval(q)
        display(grouped_df)
    #     q1=eval(q1)
    #     print(grouped_df[('Gender',     '')])
    #     print(q1.reset_index().columns,"co00lumns")
    #     print(grouped_df)
    #     return  eval(q
    #     print(grouped_df)
    #     print(q)
    #     print(len(groupby_col))
    #     grouped_df[iloc[]]
        if "groupby" in list(dic.keys()):
    #         print("ok")
    #         print(len(groupby_col))
            if len(groupby_col)==1:
                print("yes")
                col_vis1 = groupby_col 
                col_vis = "grouped_df" + str(col_vis1)

                for column, funcs in agg_col.items():
            #         print("Column:", column)
                    for func in funcs:
                        func1=f"'{func}'"
            #             print(func1)
                        col_vis=col_vis+","+"grouped_df"+f"['{column}']"+f"[{func1}]"
            #             print("Function:", func)

                col_vis="["+col_vis+"]"
    #             print(col_vis)
             
    #     print(col_vis)

    #         g["Gender"],g["Age"]["mean"],g["Income"]["mean"]]
                import group_barr

            #     print(yes)
            #     col_vis=input("Type column  saperatet by comma")

                col_vis=eval(col_vis)

            #     print(col_vis)
            #     title=input("TITLE=>")
                title=titile=my[my.index("groupby ")+8:].replace(" "," vs ").upper()

                return  group_barr.group_bar_graph(*col_vis,Title_name=title)

            else:
    #             print("wait")
                grouped_d_r=grouped_df.iloc[:,:len(groupby_col)]
                # Dropping all numeric columns
    #             grouped_d_r= grouped_d_r.select_dtypes(exclude=['number'])
    #             grouped_d_r
                # Displaying the DataFrame after dropping numeric columns
    #             print("\nDataFrame after dropping numeric columns:")
    #             print(grouped_d_r)
                list_global=[]
                legends_name=[]
                while len(list(grouped_d_r.columns))>1:
                    unique_counts = grouped_d_r.nunique()
                    min_unique_value = unique_counts.min()

                    # Find columns that have the minimum unique value count
                    min_unique_columns = unique_counts[unique_counts == min_unique_value].index

                    # Select the last column(s) among those with the same minimum unique values
                    if len(min_unique_columns) > 1:
                        col_name_min = min_unique_columns[-1]  # Choose the last column among multiple columns with the same minimum count
                    else:
                        col_name_min = min_unique_columns[0]  #
    #                 print(col_name_min,"men")
    #                 print(grouped_d_r[col_name_min[0]])
    #                 df.set_index([('Gender', ''), ('Income', ''), ('Income', 'mean')], inplace=True)

    #                 print(grouped_d_r)
                    print(grouped_df)
    #                 grouped_data_col=list(grouped_df.columns)
    #                 grouped_df=grouped_df.set_index(inplace=True)
    #                 print(grouped_df)
                    grouped_data_col=grouped_df.columns
    #                 print(grouped_data_col)
    #                 print(grouped_data_col)
    #                 print(grouped_data_col)
                    j=len(groupby_col)
    #                 print(grouped_df[("Income","")])
                    arg=1
                    while j<=len(grouped_data_col)-1:
    #                     print(len(grouped_data_col)-1)
    #                     print(j,"jjjjjjjjjjjjj")
                        for i in list(grouped_d_r[col_name_min[0]].unique()):
    #                         print(i,"male")
    #                         print("for")
    #                         print(i)
    #                         print('333',tuple(col_name_min))
    #                         print(grouped_df[grouped_df[("Gender","")]=="Female"][("Income","")])
    #                         print(grouped_df[grouped_df[tuple(col_name_min)]==i][grouped_data_col[j]],"4444444")
    #                         print(grouped_data_col[j][0],"thos")
                            globals()[f"{i}_{j}"]=grouped_df[grouped_df[tuple(col_name_min)]==i][grouped_data_col[j]]
    #                         print(grouped_df[grouped_df["Gender"]=='Female']["mean Age"],'444444')
    #                         print('col',globals()[f"{i}_{j}"])
    #                         print(female_1)
                            legends_name.append(f"{col_name_min}_{i}_{grouped_data_col[j]}")
                            list_global.append(globals()[f"{i}_{j}"])
    #                         print("global")
                            arg=arg+1
    #                         list_global1.append(grouped_df[grouped_data_col[j]].unique())

                        j=j+1

                    grouped_d_r.drop(col_name_min[0],axis=1 ,inplace=True)

    #             print("ggggggggggggggggggggggggggggggggggggggg")
    #             print(list_global,"gggggggggggggggggggggggggggggggggggggggggggggggggggg")
    #             print(grouped_d_r.iloc[:,0].unique())
                list_global.insert(0,grouped_d_r.iloc[:,0].unique())
    #             list_global=list_global+list_global1
    #             print(list_global)
                import group_bar00
                title=my[my.index("groupby ")+8:].replace(" "," vs ").upper()
                return  group_bar00.group_bar_graph(*list_global,legends_name=legends_name,Title_name=title)

        elif "groupby" not in dic.keys() and "*" in dic["select"]:
            unique_counts = grouped_df.nunique()
            col_star =list(unique_counts[unique_counts<=10].index)  # Choose the last column among multiple columns with the same minimum count
            # else:
            you_want=input("you want to see ")
            if you_want=="y" or you_want=="yes":

                for i in col_star:
                    plt.figure(figsize=(10,10))

                    plt.subplot(2,2,1)

                    print(i)

                    # here  can write and the code
                    sns.histplot(x=df[i])
                    plt.xticks(rotation=90)
                    plt.subplot(2,2,2)
                    plt.pie(x=df[i].value_counts(),labels=df[i].value_counts().index,autopct="%1.0f%%")
                    plt.show()
            else:
                print("okey")
        # here  can write and the code
    #     col_name_min = min_unique_columns[0]  
    # print(col_star)
            
#         else:
#             col_vis="grouped_df"
#             for i in dic["select"]:
#     #                 print(col_vis)
#                 col_vis=col_vis+f"['{i}']"+","

#     #                 print(col_vis)
#             # Perform operations using 'column' and 'func'
#             # For instance, you could do something like:
#             # result = your_data.groupby(groupby_col)[column].agg(func)
#             # print(result)
#             col_vis="["+ col_vis +"]"
#     #             print(col_vis)
#     #     print(col_vis)

#     #         g["Gender"],g["Age"]["mean"],g["Income"]["mean"]]
#         import group_barr

#     #     print(yes)
#     #     col_vis=input("Type column  saperatet by comma")

#         col_vis=eval(col_vis)

#     #     print(col_vis)
#     #     title=input("TITLE=>")
#         title=titile=my[my.index("groupby ")+8:].replace(" "," vs ").upper()

#         return  group_barr.group_bar_graph(*col_vis,Title_name=title)

    #     print("sorry")
    while True:


        my=input("Type Sql Syntax To Break Type N =>")
    #     my="select * from data groupby   Age      mean(Income)"
        if my.lower()=="n" or my.lower()=="no":
            break
        else:
            mysql1(my)
    # i have to make this more cleglobal()[f"{column_name_min}_{i}"]anr or the  without group datra
    # i can give the defaault argument for the legent


# In[4]:


import read
read.file_reading()
display(read.df.head())


# In[5]:


# cust=read.df


# In[7]:


run_code()



# In[ ]:


# because i did not write the  or give the space >=100 i have to write >= 100 this correct
# 


# In[2]:


import read
read.file_reading()


# In[3]:


run_code()


# In[ ]:




