-- Assignment 3 Answers for 1-5

-- 1

SELECT *
FROM products
WHERE category = 'watches'
    AND diamater = 44
    AND brand = 'Tommy Hilfiger'
    AND dial_color = 'beige';

-- 2


SELECT *
FROM (
      SELECT *
      FROM category as c
               JOIN products as p
                    ON p.category_id = c.id
               JOIN watches as wa
                    ON wa.product_id = p.id
               JOIN wine as w
                    ON w.product_id = p.id
        WHERE c.category_name = 'watches'
      ) as products
WHERE products.diamater = 44
    AND products.brand = 'Tommy Hilfiger'
    AND products.dial_color = 'beige';

-- 3

SELECT *
FROM products as p
JOIN properties as pr
    ON p.id = pr.product_id
WHERE (pr.key = 'diameter' AND pr.value = 44)
    AND (pr.key = 'brand' AND pr.value = 'Tommy Hilfiger')
    AND (pr.key = 'dial_color' AND pr.value = 'beige')


/*
 -- 4
    The simplest way to implement a similar searchable API in redis would be to on insertion:
    1) Create a hash object corresponding to a numeric key that would contain all relevant properties for the product
    2) Insert this numeric key as a value into a category key list store (i.e. watches -> [1,3,4,5,...])
    On search: We could query for the relevant product keys, then iterate over the list using python to query the product hashes
    matching the values with the search params and storing the matching keys.

 -- 5
    Mongo is fairly simple: db.products.find(
    {
        category: 'watches',
        diameter: '44',
        brand: 'Tommy Hilfiger',
        dial_color: 'beige',
    })

 For this type of data I personally would opt for a the Mongo strategy. This is because for any relational
 strategy we need some concept of product types that would need to be updated for each type. This is okay,
 but for a business like Amazon that has thousands of product types this would get cumbersome very quickly.
 Since each type has it's own properties these tables would need to be dynamic somehow, or contain a large amount of
 columns with data not relevant to their type. Mongo's dynamic schema would allow this type of data collection to grow
 and shift as needed much more easily.

 */






