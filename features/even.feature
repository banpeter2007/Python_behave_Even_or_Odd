Feature: Páros szám ellenőrzése

  # TODO: Írd ide a scenariókat!
  # 1. Páros szám ellenőrzése (pl. 4)
  # 2. Páratlan szám ellenőrzése (pl. 5)
  # 3. Nulla ellenőrzése (0)
  # 4. Negatív páros szám ellenőrzése (-4)
  # 5. Negatív páratlan szám ellenőrzése (-5)

  Scenario: Páros szám ellenőrzése
    Given the number is 4
    When I check the number
    Then I should told "even"