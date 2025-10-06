# importing the numpy library first
import numpy as np

#function to simulate a throwing die n times in python
def throw_die(n):
  return np.random.randint(1,7, n)

#function to calculate the probability of each face in the simulation
def calculate_probabilities(throws):
  count = np.bincount (throws, minlength = 7)[1:] # counting occurences of each face (1 to 6)
  probabilities = count / len(throws) #probability of each face
  return probabilities


# theoretical probability for a fair die
theoretical_probabilities = np.array ([1/6]* 6)

#simulate die throws for 10, 50 and 100 times

throws_10 = throw_die(10)
throws_50 = throw_die(50)
throws_100 = throw_die(100)

#calculate monte carlo probabilities for each set of throws
monte_carlo_10 = calculate_probabilities(throws_10)
monte_carlo_50 = calculate_probabilities(throws_50)
monte_carlo_100 = calculate_probabilities(throws_100)

# print separate results for theoretical and Monte Carlo probabilities for each case
print ("Result for 10 throws: ")
print ("Theoretical Probabilities: ")
print (f"1: {theoretical_probabilities[0]: .2f} , 2: {theoretical_probabilities[1]: .2f}, 3: {theoretical_probabilities[2]: .2f}, 4: {theoretical_probabilities[3]: .2f}, 5: {theoretical_probabilities[4]: .2f}, 6: {theoretical_probabilities[5]: .2f}")
print ("Monte Carlo Probabilities: ")
print (f"1: {monte_carlo_10[0]: .2f} , 2: {monte_carlo_10[1]: .2f}, 3: {monte_carlo_10[2]: .2f}, 4: {monte_carlo_10[3]: .2f}, 5: {monte_carlo_10[4]: .2f}, 6: {monte_carlo_10[5]: .2f}")


print ("\n Result for 50 throws: ") 
print ("Theoretical Probabilities: ")
print (f"1: {theoretical_probabilities[0]: .2f} , 2: {theoretical_probabilities[1]: .2f}, 3: {theoretical_probabilities[2]: .2f}, 4: {theoretical_probabilities[3]: .2f}, 5: {theoretical_probabilities[4]: .2f}, 6: {theoretical_probabilities[5]: .2f}")  
print ("Monte Carlo Probabilities: ")
print (f"1: {monte_carlo_50[0]: .2f} , 2: {monte_carlo_50[1]: .2f}, 3: {monte_carlo_50[2]: .2f}, 4: {monte_carlo_50[3]: .2f}, 5: {monte_carlo_50[4]: .2f}, 6: {monte_carlo_50[5]: .2f}")    

print ("\n Result for 100 throws: ")
print ("Theoretical Probabilities: ")
print (f"1: {theoretical_probabilities[0]: .2f} , 2: {theoretical_probabilities[1]: .2f}, 3: {theoretical_probabilities[2]: .2f}, 4: {theoretical_probabilities[3]: .2f}, 5: {theoretical_probabilities[4]: .2f}, 6: {theoretical_probabilities[5]: .2f}")
print ("Monte Carlo Probabilities: ")
print (f"1: {monte_carlo_100[0]: .2f} , 2: {monte_carlo_100[1]: .2f}, 3: {monte_carlo_100[2]: .2f}, 4: {monte_carlo_100[3]: .2f}, 5: {monte_carlo_100[4]: .2f}, 6: {monte_carlo_100[5]: .2f}")