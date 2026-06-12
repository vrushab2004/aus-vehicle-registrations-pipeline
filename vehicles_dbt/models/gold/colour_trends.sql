with base as (
    select * from {{ref('stg_vehicles')}}
),

aggregated as (
    select
        color_code,
        sum(units_registered) as total_units,
    from base
    group by color_code
)

select * from aggregated
order by total_units desc
