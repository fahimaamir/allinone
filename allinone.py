import streamlit as st
import pandas as pd
from st_aggrid import AgGrid, GridOptionsBuilder
from st_aggrid import AgGrid, GridOptionsBuilder, GridUpdateMode, DataReturnMode
#from pivottablejs import pivot_ui
from st_aggrid import AgGrid, GridOptionsBuilder, GridUpdateMode, DataReturnMode
from st_aggrid import AgGrid, GridOptionsBuilder, JsCode
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, ColumnsAutoSizeMode
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode
from st_aggrid import JsCode, AgGrid, GridOptionsBuilder
from st_aggrid.shared import ColumnsAutoSizeMode
from st_aggrid.shared import GridUpdateMode
import numpy as np
import os
import pandas as pd
import streamlit as st
import streamlit.components.v1 as components
import streamlit as st
import numpy as np
import pandas as pd
from streamlit_dynamic_filters import DynamicFilters
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode
from st_aggrid.shared import ColumnsAutoSizeMode
import openpyxl

st.html("""
    <style>
        .stMainBlockContainer {
            max-width:350rem;
            max-hight:10rem;
        }
    </style>
    """
)

#st.set_page_config(layout="wide")

data = {
    'region': ['North America', 'North America', 'Europe', 'Oceania',
               'North America', 'North America', 'Europe', 'Oceania',
               'North America', 'North America', 'Europe', 'Oceania'],
    'country': ['USA', 'Canada', 'UK', 'Australia',
                'USA', 'Canada', 'UK', 'Australia',
                'USA', 'Canada', 'UK', 'Australia'],
    'city': ['New York', 'Toronto', 'London', 'Sydney',
             'New York', 'Toronto', 'London', 'Sydney',
             'New York', 'Toronto', 'London', 'Sydney'],
    'population': [6575, 45645, 345345, 345345,
             23426, 234234, 34534, 345345,
             23423, 34324, 23424, 23423],
    
    'district': ['Manhattan', 'Downtown', 'Westminster', 'CBD',
                 'Brooklyn', 'Midtown', 'Kensington', 'Circular Quay',
                 'Queens', 'Uptown', 'Camden', 'Bondi']
}


st.header('Diffrent type data Filter   ')

with st.expander("Expander 00000000000000000001: Click to reveal content"):
        st.write('Muhammad is the Best')
        def generate_sales_data():
            """Generate dataset simulating sales data."""
            np.random.seed(42)
            rows = 50

            # Create a more complex dataset
            df = pd.DataFrame({
                'Product_ID': range(1, rows + 1),
                'City': np.random.choice(['Karachi', 'Islamabad', 'Quata', 'Pishawar'], rows),
                'Category': np.random.choice(['Electronics', 'Clothing', 'Home', 'Sports'], rows),
                'Item': np.random.choice(['IRON', 'pant', 'Flate', 'football'], rows),
                'Sale_person': np.random.choice(['Fahim', 'Aamir', 'Zahir', 'Asim'], rows),
                'Base_Price': np.random.uniform(10, 500, rows).round(2),
                'Quantity_Sold': np.random.randint(1, 100, rows),
                'commission': np.random.randint(100, 1000, rows),
            })

            return df


        def configure_grid_options(df):
                """Configure advanced grid options with multiple features."""
                gb = GridOptionsBuilder.from_dataframe(df)
                # Configure row grouping and aggregation
                #gb.configure_column("allColumns", filter=True)
                for column in df.columns:
                    gb.configure_column(column, filter=True)

                gb.configure_default_column(
                            groupable=True,
                            value=True,
                            enableRowGroup=True,
                            aggFunc='sum'
                        )

                        # Add filter and sort options
                gb.configure_grid_options(
                            enableRangeSelection=True,
                            enableRangeHandle=True,
                            suppressColumnMoveAnimation=False,
                            suppressRowClickSelection=False
                        )
                
                return gb.build()
        sales_data = generate_sales_data()

        grid_options = configure_grid_options(sales_data)
        gb = GridOptionsBuilder()
        gb.configure_default_column( groupable=True,value=True,enableRowGroup=True,aggFunc='sum'  )

                        # Add filter and sort options
        gb.configure_grid_options(
                            enableRangeSelection=True,
                            enableRangeHandle=True,
                            #allColumnsfilter=True,
                            #gob.configure_column("allColumns", filter=True)
                            suppressColumnMoveAnimation=False,
                            suppressRowClickSelection=False)
        gb.build()

                

            #st.subheader('Interactive Sales Data Grid')
        st.markdown("""
            **Features:**
            - Edit Base Price and Quantity Sold
            - Automatic Total Revenue calculation
            """)







            # AgGrid with custom options
        mfa = AgGrid(
                sales_data,
                gridOptions=grid_options,
                height=500,
                theme='alpine',
                allow_unsafe_jscode=True,
                #update_mode=GridUpdateMode.MODEL_CHANGED,
                update_mode=GridUpdateMode.GRID_CHANGED,
                data_return_mode=DataReturnMode.FILTERED_AND_SORTED,
                fit_columns_on_grid_load=True,
                width =2900 ,
                reload_data=False
            )


        #if st.button('Check availability'):
        mfa4 =mfa['data']
        forpivot =mfa['data']
        st.write(mfa4)


        #st.expander("See explanation"):   
        colname = list(mfa4)

        col1, col2, col3 = st.columns(3)

        col1.write('Rows')
        col2.write('Columns')
        col3.write('Values')

        with col1:
            options = st.multiselect(    "What are your favorite colors?",    colname,    default=colname[0], )
        with col2:
            options1 = st.multiselect(    "What are your favorite colors?",    colname,    default=colname[1], )
        with col3:
            options2 = st.multiselect(    "What are your favorite colors?",    colname,    default=colname[-1], )
            
        if st.button('Group by'):
            #st.write("Muhammad")
            
            #df.groupby(['Animal']).mean()
            #aggregated_data = mfa4.groupby(options).agg(options2,'sum')


            a,  *rest = options2
            #aggregated_data = mfa4.groupby(options).agg(a,'sum')
            #aggregated_data = mfa4.groupby('city').agg('commission','sum')
            df_grouped = (mfa4.groupby(options)   [a].sum()).reset_index()
            #df.groupby('A').B.agg(['min', 'max'])
            #df.groupby("A")[["B"]].agg(lambda x: x.astype(float).min())
            #df2.groupby(["X"], sort=False).sum()
            st.write(df_grouped)
            #aggregated_data = mfa4.groupby(options).agg(total_salary=(options2, 'sum'))
            #aggregated_data = mfa4.groupby('city').agg(total_salary=('commission', 'sum'))
            #st.write(aggregated_data)
            
            #total_salary=('Salary', 'sum'),
            #avg_salary=('Salary', 'mean'),
            #player_count=('Name', 'count')
            
            #https://stackoverflow.com/questions/66350904/pandas-subtotal-similar-to-excel
        if st.button('Pivot Table'):
            #muhammad = pd.pivot_table(mfa,values="QTY",index=['ITME'], columns='BOOMSIZE',aggfunc='sum')
            muhammad = pd.pivot_table(mfa4,values=options2,index=options, columns=options1,aggfunc='sum')
            #df3 = mfa4.pivot(index=value1, columns=value2 ,values=value3,aggfunc='sum')
            #os.remove('pivott.csv') 
            st.write(muhammad)
            pcsv = muhammad.to_csv(index=True).encode('utf-8')
            #pcsv = muhammad.to_csv().encode('utf-8')
            
            #csv = convert_df(pcsv)

            st.download_button(
                label="Pivot data as CSV",
                data=pcsv,
                file_name='pivottable.csv',
                mime='text/csv',         )
        if st.button('Dynamic Pivot'):
            st.write("muhammad")
        #    t = pivot_ui(sales_data)

        #   with open(t.src) as t:
        #      components.html(t.read(), width=4900, height=1000, scrolling=True)
                #components.html(t.read(), width=3900,  scrolling=True)


with st.expander("Expander 111111111111111111111111111111: Click to reveal content"):
    df = pd.DataFrame(data)
    dynamic_filters = DynamicFilters(df, filters=['region', 'country', 'city','population' , 'district'])
    st.write("Apply filters in any order 👇")
    dynamic_filters.display_filters(location='columns', num_columns=2, gap='large')
    dynamic_filters.display_df()
    tdf = pd.DataFrame(dynamic_filters.filter_df())
    col_lst = tdf.columns.to_list()
    col_lst = {col_lst[i]: True for i in range(len(col_lst))}

    sc1, sc2 = st.columns((2,8), vertical_alignment='bottom')
    sc1.write("Select Cols:")
    for k, v in col_lst.items(): col_lst[k] = sc1.checkbox(label=k, value=v)
    sc2.dataframe(tdf[[key for key, value in col_lst.items() if value]], use_container_width=False)
    df3 = pd.DataFrame(col_lst.items())
    df3.columns = ['Colname', 'Cstatus']
    result_df= df3.loc[df3['Cstatus']==True]
    single_column_series = result_df['Colname'].values.tolist()
    df4 = pd.DataFrame(tdf, columns=single_column_series)
    st.write(df4)

    if st.button('Check availability'):
        st.write('Muhammad is the Best -------- for graph ')
        st.bar_chart(df4)
        st.area_chart(df4)
        st.line_chart(df4)


with st.expander("Expander 222222222222222222222222222 ----------: Click to reveal content"):
    mfa2 = pd.DataFrame(data)
    gb = GridOptionsBuilder.from_dataframe(mfa2)
    gb.configure_selection(
            selection_mode="multiple",
            use_checkbox=True,
            pre_selected_rows=None,  # <-- Set to manually persist checkbox state
        )
    for column in mfa2.columns:
                gb.configure_column(column, filter=True)

    gridOptions = gb.build()
    mfa = AgGrid(
            mfa2,
            gridOptions=gridOptions,
            update_mode=GridUpdateMode.GRID_CHANGED,
            columns_auto_size_mode=ColumnsAutoSizeMode.FIT_CONTENTS,
            data_return_mode=DataReturnMode.FILTERED   # <-- Gets filtered data, but not filters applied to columns
        )

    selected_rows = mfa['selected_rows']

    if st.button('filter with graph'):
        mfa4 =mfa['data']
        fild = pd.DataFrame(mfa['columns_state'])
        above_35= fild["hide"] 
        above_36= fild["colId"] 
        list_from_df = above_36.values.tolist()
        list_from_column = fild["colId"].tolist()
        
        fild["hide"] = fild["hide"].astype(int) 
        fild = fild[fild["hide"]==0 ]
        list_from_df2 = fild["colId"].values.tolist()
        
        mfa5 = mfa4[list_from_column]
        mfa6 = mfa4[list_from_df2]
        mfa7 = pd.DataFrame(mfa6)
        mfa7.set_index(mfa6.iloc[:,0], inplace=True)
        st.write(mfa6)
        #st.write(mfa7)
        first_column_name = mfa7.columns[0]
        st.bar_chart(mfa6)
        st.area_chart(mfa6)
        st.line_chart(mfa6)
        st.pyplot(mfa6.plot.barh(stacked=True).figure)
        st.pyplot(mfa7.plot.bar(stacked=True).figure)
        st.pyplot(mfa7.plot.bar(rot=0).figure)
    else:

        st.warning("you need to upload a excel file.")



    st.dataframe(pd.DataFrame(selected_rows))



with st.expander("Expander 333333333333333333333333333333333 ----------: Click to reveal content"):
    
    # Load your dataset
    #df = pd.read_json("https://www.ag-grid.com/example-assets/olympic-winners.json")
    df = pd.DataFrame(data)
    # Configure grid options
    gb = GridOptionsBuilder.from_dataframe(df)
    
    
    for column in df.columns:
                gb.configure_column(column, filter=True)

    gb.configure_default_column(
        groupable=True,
        value=True,
        enableRowGroup=True,
        aggFunc='sum'
    )

    # Customize specific column behaviors
    gb.configure_column('country', header_name="Home Country")
    gb.configure_pagination(enabled=True, paginationPageSize=5)
    gb.configure_selection(selection_mode="multiple", use_checkbox=True)
    gb.configure_side_bar(filters_panel=True, defaultToolPanel='filters')

    # Build the final option object
    grid_options = gb.build()

    # Render AgGrid
    mfatt = AgGrid(
        df,
        gridOptions=grid_options,
        height=400,
        width='100%',
        allow_unsafe_jscode=True,
            
    #    gridOptions=gridoptions,
        enable_enterprise_modules=True,
        update_mode=GridUpdateMode.MODEL_CHANGED,
        data_return_mode=DataReturnMode.FILTERED_AND_SORTED,
        fit_columns_on_grid_load=False,
        header_checkbox_selection_filtered_only=True,
        use_checkbox=True)
        


    st.markdown("### All Possible builder options")
    for p in dir(GridOptionsBuilder):
        if not p.startswith("_"):
            _ = gb.__getattribute__(p)
            #st.write(_)
            
            
    cap_button = st.button("Start Capturing") # Give button a variable name
    if cap_button: # Make button a condition.
        st.write("muhammad is the best")
        #st.write(mfatt['selected_rows'])
        #st.write(mfatt['data'])
        #st.datagrame(mfatt("data"))
        ###https://docs.google.com/spreadsheets/d/1vu-5QOoLpir98duhVuumD0ABr_kZCww2/edit?usp=sharing&ouid=106062244503517417798&rtpof=true&sd=true
        #https://docs.google.com/spreadsheets/d/10QnGoTTz3ZsgxiTliIbJ8yk36s1BUu7WlDi9kZhMQS0/edit?usp=sharing
        #https://docs.google.com/spreadsheets/d/10QnGoTTz3ZsgxiTliIbJ8yk36s1BUu7WlDi9kZhMQS0/edit?gid=858585402#gid=858585402
        
        #https://docs.google.com/spreadsheets/d/10uBt4S7CRmfTV4vEGniqPA0igXz9Ywti/edit?usp=sharing&ouid=105182257404870437876&rtpof=true&sd=true
        #https://docs.google.com/spreadsheets/d/10QnGoTTz3ZsgxiTliIbJ8yk36s1BUu7WlDi9kZhMQS0/edit?usp=sharing
        url1 = "https://docs.google.com/spreadsheets/d/10QnGoTTz3ZsgxiTliIbJ8yk36s1BUu7WlDi9kZhMQS0/edit?usp=sharing"
        file_id12 = url1.split("/")[-2]
        path112 = "https://drive.google.com/uc?export=download&id=" + file_id12
        #sce = pd.read_excel(path1)
        #st.session_state.df92 = pd.read_excel(path112)
        #st.write(st.session_state.df92 )
        #data = st.session_state.df92
    #    data3 = data.pivot_table(index='Country', columns='City', values='salary')
    #   st.write(data3)