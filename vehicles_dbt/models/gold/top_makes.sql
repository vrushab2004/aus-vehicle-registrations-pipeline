with base as (
    select * from {{ ref('stg_vehicles') }} -- this gets the data from silver(view) model we did in staging.
),

aggregated as (
    select
        make,
        sum(units_registered) as total_units, -- total vehicles registeredper brand
        count (distinct model) as total_models, -- total unique models per brand 
        sum (case when manufacture_year = 2026 then units_registered else 0 end) as units_2026, --units registered in 2026
        sum (case when manufacture_year = 2025 then units_registered else 0 end) as units_2025 --units registered in 2025
    from base
    group by make
)

select * from aggregated
order by total_units desc -- order the results by total units registered in descending order.