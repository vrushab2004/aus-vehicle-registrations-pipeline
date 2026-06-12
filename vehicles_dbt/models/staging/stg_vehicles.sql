with source as(
    select * from {{ source('vehicles', 'vehicles_raw') }}
), -- go get all the raw data from bigquery and put it in a CTE called source

renamed as (
    select trim(CLEAN_MAKE_VEH) AS make, -- trim() is used to remove any spaces from the string values.
           trim(CD_MODEL_VEH) AS model,
           trim(CD_CLR_BDY_VEH_P) AS color_code,
           NB_YEAR_MFC_VEH AS manufacture_year, -- this is a numeric field so we do not need to trim it.
           TOTAL AS units_registered
    from source -- As we have initialised this above.
           
)

select * from renamed -- return the cleaned version as final result.