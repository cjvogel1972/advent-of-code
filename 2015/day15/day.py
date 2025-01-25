import re

PARSER = re.compile(r"\w+: capacity (-?\d+), durability (-?\d+), flavor (-?\d+), texture (-?\d+), calories (-?\d+)")


def solve_part1(lines: list[str]) -> int:
    ingredients, measurements = prepare_ingredients_measurements(lines)

    max_score = 0
    while True:
        cap_score, dur_score, fla_score, tex_score, _ = compute_cookie_scores(measurements, ingredients)
        score = cap_score * dur_score * fla_score * tex_score
        max_score = max(score, max_score)

        if measurements[0] == 100:
            break

        increment_measurements(measurements)

    return max_score


def solve_part2(lines: list[str]) -> int:
    ingredients, measurements = prepare_ingredients_measurements(lines)

    max_score = 0
    while True:
        cap_score, dur_score, fla_score, tex_score, calories = compute_cookie_scores(measurements, ingredients)
        if calories == 500:
            score = cap_score * dur_score * fla_score * tex_score
            max_score = max(score, max_score)

        if measurements[0] == 100:
            break

        increment_measurements(measurements)

    return max_score


def prepare_ingredients_measurements(lines):
    ingredients = []
    measurements = []

    for line in lines:
        scores = map(int, PARSER.match(line).groups())
        ingredients.append(compute_ingredient_scores(*scores))
        measurements.append(0)

    measurements[-1] = 100

    return ingredients, measurements


def compute_ingredient_scores(capacity, durability, flavor, texture, calories) -> dict:
    cap = []
    dur = []
    fla = []
    tex = []
    cal = []

    for teaspoons in range(101):
        cap.append(teaspoons * capacity)
        dur.append(teaspoons * durability)
        fla.append(teaspoons * flavor)
        tex.append(teaspoons * texture)
        cal.append(teaspoons * calories)

    return {'capacity': cap, 'durability': dur, 'flavor': fla, 'texture': tex, 'calories': cal}


def compute_cookie_scores(measurements, ingredients):
    cap_score = 0
    dur_score = 0
    fla_score = 0
    tex_score = 0
    calories = 0

    for i, teaspoons in enumerate(measurements):
        ingredient = ingredients[i]
        cap_score += ingredient['capacity'][teaspoons]
        dur_score += ingredient['durability'][teaspoons]
        fla_score += ingredient['flavor'][teaspoons]
        tex_score += ingredient['texture'][teaspoons]
        calories += ingredient['calories'][teaspoons]

    if cap_score < 0:
        cap_score = 0
    if dur_score < 0:
        dur_score = 0
    if fla_score < 0:
        fla_score = 0
    if tex_score < 0:
        tex_score = 0

    return cap_score, dur_score, fla_score, tex_score, calories


def increment_measurements(measurements: list[int]):
    while True:
        for i in range(len(measurements) - 2, -1, -1):
            measurements[i] += 1
            if measurements[i] <= 100:
                break
            measurements[i] = 0

        measurements[-1] = (100 - sum(measurements[:-1])) if sum(measurements[:-1]) < 100 else 0
        if sum(measurements) == 100:
            break
