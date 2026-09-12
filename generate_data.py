from pathlib import Path


topics = {
    "space": [
        "Space exploration involves studying planets, stars, galaxies, and the universe.",
        "Rocket technology allows spacecraft to travel beyond Earth and conduct scientific missions.",
        "Astronomers use telescopes to study distant celestial objects and understand cosmic evolution.",
        "Mars missions investigate the planet's atmosphere, geology, and possibility of ancient life.",
    ],

    "artificial_intelligence": [
        "Artificial intelligence allows computers to perform tasks that normally require human intelligence.",
        "Machine learning systems learn patterns from data and use those patterns to make predictions.",
        "Neural networks are computational models inspired by biological neurons.",
        "Generative AI can produce text, images, audio, and software from user instructions.",
    ],

    "programming": [
        "Python is a popular programming language used for automation, data science, and artificial intelligence.",
        "JavaScript is widely used to build interactive websites and web applications.",
        "Software engineers use algorithms and data structures to solve computational problems.",
        "Version control systems help developers track changes and collaborate on software projects.",
    ],

    "history": [
        "Ancient civilizations developed cities, writing systems, trade networks, and complex governments.",
        "The Industrial Revolution transformed manufacturing through machines and new production methods.",
        "World War history influenced international politics, economics, and technological development.",
        "Archaeologists study artifacts and ruins to understand how earlier societies lived.",
    ],

    "environment": [
        "Climate change is influenced by greenhouse gas emissions and changes in Earth's atmosphere.",
        "Renewable energy includes solar, wind, hydroelectric, and geothermal power.",
        "Forests support biodiversity and play an important role in the global carbon cycle.",
        "Ocean pollution can damage marine ecosystems and affect wildlife.",
    ],

    "business": [
        "Businesses analyze customers, markets, competitors, and revenue to make strategic decisions.",
        "Marketing helps organizations communicate the value of products and services.",
        "Entrepreneurs create companies by identifying problems and developing useful solutions.",
        "Financial planning helps companies manage costs, investments, and cash flow.",
    ],

    "health": [
        "Regular physical activity supports cardiovascular health and overall fitness.",
        "A balanced diet provides the nutrients required for normal body functions.",
        "Sleep plays an important role in memory, recovery, and daily performance.",
        "Public health programs focus on disease prevention and improving community wellbeing.",
    ],

    "education": [
        "Students learn effectively when concepts are explained clearly and practiced regularly.",
        "Online education provides access to courses and learning resources from many locations.",
        "Universities conduct research while providing academic and professional training.",
        "Project-based learning allows students to apply theoretical concepts to practical problems.",
    ],

    "sports": [
        "Football requires teamwork, tactical planning, fitness, and technical ability.",
        "Cricket combines batting, bowling, fielding, and strategic decision making.",
        "Athletes improve performance through training, recovery, nutrition, and competition.",
        "Team sports require communication and coordination between players.",
    ],

    "finance": [
        "Investing involves balancing expected returns against financial risk.",
        "Banks provide services such as deposits, loans, payments, and financial management.",
        "Personal budgeting helps individuals track income, expenses, and savings.",
        "Financial markets allow investors to trade assets such as stocks and bonds.",
    ]
}


data_dir = Path("data")
data_dir.mkdir(exist_ok=True)

counter = 1

for topic, paragraphs in topics.items():

    for variation in range(10):

        content = (
            f"Topic: {topic.replace('_', ' ').title()}\n\n"
            + "\n\n".join(paragraphs)
            + f"\n\nThis document provides an overview of "
              f"{topic.replace('_', ' ')} and related concepts. "
              f"Example document variation {variation + 1}."
        )

        filename = data_dir / f"{topic}_{variation + 1:02d}.txt"

        filename.write_text(
            content,
            encoding="utf-8"
        )

        counter += 1

print(f"Created {counter - 1} documents.")