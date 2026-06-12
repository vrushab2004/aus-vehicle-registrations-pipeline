-- Step 1: get all the cleaned data
with base as (
    select * from {{ ref('stg_vehicles') }}
),

-- Step 2: count units per brand + colour combination
aggregated as (
    select
        make,
        color_code,
        sum(units_registered) as total_units
    from base
    group by make, color_code
),

-- Step 3: number the colours within each brand (1 = most popular)
ranked as (
    select
        *,
        rank() over (
            partition by make        -- within each brand
            order by total_units desc -- most units = rank 1
        ) as colour_rank,
        sum(total_units) over (
            partition by make        
        ) as make_total_units     
    from aggregated
)

-- Step 4: only keep rank 1 (most popular colour per brand)
select make, color_code, total_units , make_total_units
from ranked
where colour_rank = 1
order by total_units desc