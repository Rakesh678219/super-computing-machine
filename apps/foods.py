from os import times
import streamlit as st
import time


def app():
    def draw_all(
        key,
        plot=False,
    ):
        col1, col2, col3 = st.beta_columns([1, 4.5, 1])

        with col1:
            st.write("")

        with col2:
            st.image('rvce.png')

        with col3:
            st.write("")

        st.write(
            """
            # Minor Project On ML
            
            """
        )
        st.write("#")
        st.header("Contributed by")
        st.write(
            """
            **Pavankalyan D S  - 1RV18EC108**\n
            **Rakesh Reddy P -  1RV18EC109**\n
            **Prajwal  B  Raj -  1RV18EC111** \n
            **Pratheek J Bhat -  1RV18EC105**\n
            
            """
        )
        st.write("#")
        st.header("Guided by")
        st.write(
            """
            **Rajani Katiyar, Assistant Professor, Electronics and Communication Engineering.** 
            """
        )

    with st.sidebar:
        draw_all("sidebar")
    st.image('food_images/good foods/good foods.jpg')
    st.title('10 Foods That Are Good for Your Eyes')

    st.header('1 Raw Red Peppers')
    st.image('food_images/good foods/Raw Red Peppers.png')
    st.subheader('Bell peppers give you the most vitamin C per calorie. That is good for the blood vessels in your eyes, and science suggests it could lower your risk of getting cataracts. It is found in many vegetables and fruits, including bok choy, cauliflower, papayas, and strawberries. Heat will break down vitamin C, so go raw when you can. Brightly colored peppers also pack eye-friendly vitamins A and E')

    st.header('2 Sunflower Seeds and Nuts')
    st.image('food_images/good foods/Sun flower seeds.png')
    st.subheader('An ounce of these seeds or almonds has half the amount of vitamin E the USDA recommends for adults each day. A large study found that vitamin E, together with other nutrients, can help slow age-related macular degeneration (AMD) from getting worse. It may also help prevent cataracts. Hazelnuts, peanuts (technically legumes), and peanut butter are also good sources of vitamin E')

    st.header('3 Dark, Leafy Greens')
    st.image('food_images/good foods/Dark Leady Greens.png')
    st.subheader('Kale, spinach, and collard greens, for example, are rich in both vitamins C and E. They also have the carotenoids lutein and zeaxanthin. These plant-based forms of vitamin A lower your risk of long-term eye diseases, including AMD and cataracts. Most people who eat Western diets do not get enough of them')

    st.header('4 Salmon')
    st.image('food_images/good foods/Salmon.png')
    st.subheader('Your retinas need two types of omega-3 fatty acids to work right: DHA and EPA. You can find both in fatty fish, such as salmon, tuna, and trout, as well as other seafood. Omega-3s also seem to protect your eyes from AMD and glaucoma. Low levels of these fatty acids have been linked to dry eyes.')

    st.header('5 Sweet Potatoes')
    st.image('food_images/good foods/Sweet Potatoes.png')
    st.subheader('Orange-colored fruits and vegetables -- like sweet potatoes, carrots, cantaloupe, mangos, and apricots -- are high in beta-carotene, a form of vitamin A that helps with night vision, your eyes ability to adjust to darkness. One sweet potato also has more than half the vitamin C you need in a day and a little vitamin E')

    st.header('6 Lean Meat and Poultry')
    st.image('food_images/good foods/Lean Meat and Porultry.png')
    st.subheader('Zinc brings vitamin A from your liver to your retina, where it is used to make the protective pigment melanin. Oysters have more zinc per serving than any other food, but you do not have to be a shellfish lover to get enough: Beef, pork, and chicken (both dark and breast meat) are all good sources')

    st.header('7 Beans and Legumes')
    st.image('food_images/good foods/Beans and Legumes.png')
    st.subheader('Prefer a vegetarian, low-fat, high-fiber option to help keep your vision sharp at night and slow AMD? Chickpeas are also high in zinc, as are black-eyed peas, kidney beans, and lentils. A can of baked beans will do the job, too.')

    st.header('8 Eggs')
    st.image('food_images/good foods/Eggs.png')
    st.subheader('It is a great package deal: The zinc in an egg will help your body use the lutein and zeaxanthin from its yolk. The yellow-orange color of these compounds blocks harmful blue light from damaging your retina. They help boost the amount of protective pigment in the macula, the part of your eye that controls central vision')

    st.header('9 Squash')
    st.image('food_images/good foods/Squash.png')
    st.subheader('Your body cannot make lutein and zeaxanthin, but you can get them from squash all year long. Summer squash also has vitamin C and zinc. The winter kind will give you vitamins A and C as well as omega-3 fatty acids, too')

    st.header('10 Broccoli and Brussels Sprouts')
    st.image('food_images/good foods/Brocolli.png')
    st.subheader('These related veggies come with another winning combination of nutrients: vitamin A (as lutein, zeaxanthin, and beta-carotene), vitamin C, and vitamin E. They are all antioxidants that protect the cells in your eyes from free radicals, a type of unstable molecule that breaks down healthy tissue. Your retinas are especially vulnerable.')
