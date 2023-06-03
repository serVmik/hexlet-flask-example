from faker import Faker


fake = Faker()
Faker.seed(1234)


def generate(size):
    posts = []
    for _ in range(size):
        posts.append({
            'id': fake.uuid4(),
            'title': fake.sentence(),
            'body': fake.text(),
            'slug': fake.slug(),
            })
    return posts
