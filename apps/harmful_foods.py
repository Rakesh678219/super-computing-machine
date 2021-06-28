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
    st.title('Foods That May Harm Your Eyes')
    st.image('food_images/Bad foods/Foods for ur eyes.png')
    st.header('Food and Your Eyes')
    st.subheader('About 250 million people around the world have mild to serious vision loss. Did you know that the health of your eyes is directly connected to the health of your heart and blood vessels?  What you eat and drink can have a lasting impact on both your cardiovascular health and your vision.')

    st.header('1 Bread And Pasta')
    st.image('food_images/Bad foods/Bread and Pasta.png')
    st.subheader('Researchers have linked simple carbohydrates, like those found in white bread and pasta, with a higher chance of age-related macular degeneration (AMD), a leading cause of vision loss for older adults. The reason: Your body digests this type of carb quickly. This causes a spike in blood sugar. To prevent this, health experts suggest that you swap white bread and pasta for whole-grain versions')

    st.header('2 Processed Meats')
    st.image('food_images/Bad foods/Processed meats.png')
    st.subheader('Hot dogs, bacon, and deli meats are loaded with sodium. This salt spike can eventually lead to high blood pressure (hypertension). In your eyes, this may cause Hypertensive retinopathy, blood vessel damage that causes blurred vision or vision loss , a buildup of fluid beneath the retina Neuropathy, a blockage of blood flow that kills nerves and causes vision loss Try to limit your sodium to 2,300 milligrams or less a day.')

    st.header('3 Fried Foods')
    st.image('food_images/Bad foods/Fried foods.png')
    st.subheader('Deep-fried foods cooked in trans fats raise your LDL (“bad”) cholesterol levels and could lead to heart disease, stroke, and type 2 diabetes. They also create molecules called free radicals that can damage and kill cells. This all connects to eye disease -- AMD and diabetic retinopathy. Fight back against free radicals by eating fruits and veggies full of vitamin C like citrus fruits, tomatoes, and red bell peppers')

    st.header('4 Cooking Oils')
    st.image('food_images/Bad foods/Cooking oils.png')
    st.subheader('A landmark study 30 years ago linked too much linoleic acid, a type of unsaturated fat, with a higher chance of AMD. You can find it in these cooking oils:Safflower , Sunflower ,Corn , Soybean ,Sesame,Health experts suggest cooking oils with less than 4 grams of saturated fat per tablespoon. Stay away from ones with hydrogenated oils and trans fats.')

    st.header('5 Margarine')
    st.image('food_images/Bad foods/Margarine.png')
    st.subheader('It’s made with vegetable oils, so it has unsaturated “good” fats. All things considered, it may be better for you than butter. But some margarine also has trans fat, which raises your cholesterol levels and the chance of heart disease and eye problems. The more solid the margarine, the more trans fat it has. Instead of a stick, use the spread or liquid kind. You can also look for brands with 0 grams of trans fat on the label')

    st.header('6 Ready-to-Eat Foods')
    st.image('food_images/Bad foods/Ready-to-Eat Foods.png')
    st.subheader('Prepackaged foods -- things like soup, tomato sauce, and canned goods -- often have high amounts of sodium, up to 75% of the suggested amount. Eating less of these foods can lower your chance of high blood pressure and related eye problems. When you shop, look for “low sodium” or “no salt added” versions of your favorite foods. Add your own spices and herbs for a natural flavor boost. ')

    st.header('7 Sugary Drinks')
    st.image('food_images/Bad foods/Sugary Drinks.png')
    st.subheader('Soda, sports and energy drinks, lemonade, and other sweetened drinks are full of sugar -- sometimes 7 to 10 teaspoons. They’re also the number one source of calories and added sugar in the U.S. diet. All that sugar ups your odds of type 2 diabetes and heart disease. This can lead to related eye conditions like diabetic retinopathy and AMD. Water is your best bet for a healthy drink.')

    st.header('8 Fish and Shellfish')
    st.image('food_images/Bad foods/Fish and Shellfish.png')
    st.subheader('Most of us have no reason to worry about the mercury in fish and shellfish in moderation. But at high levels and for certain groups of people, it can cause serious health problems, including eye damage. Health experts say pregnant women, those who are nursing or may become pregnant, and children should stick with 8-12 ounces of fish and shellfish each week.')

    st.header('9 Alcohol')
    st.image('food_images/Bad foods/Alcohol.png')
    st.subheader('While not a food, alcohol is something you put into your body that experts link to eye disease. Drinking too much alcohol can lead to cataracts at an earlier age, a common condition that causes a cloudy area in your eye lens.')

    st.header('10 Caffeine')
    st.image('food_images/Bad foods/Caffine.png')
    st.subheader('The caffeine in your morning cup of coffee or tea may raise the pressure inside your eye, or intraocular pressure (IOP). Studies show this pressure goes up in people with glaucoma or ocular hypertension (OHT) who’ve had caffeine. IOP that’s too high can cause vision loss and blindness.')
