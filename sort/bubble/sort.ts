function bubbleSort(numbers:number[]):number[]{
  const lenNumbers = numbers.length;
  for(let i = 0; i<lenNumbers;i++){
    for(let j =0; j<lenNumbers -1-j; j++){
      if(numbers[j]>numbers[j+1]){
        [numbers[j],numbers[j+1]] = [numbers[j+1],numbers[j]]
      }
    }
  }
  return numbers
}

function getRandomNumbers(count: number, max: number): number[] {
  const nums: number[] = [];
  for (let i = 0; i < count; i++) {
    nums.push(Math.floor(Math.random() * max));
  }
  return nums;
}

const nums = getRandomNumbers(10, 1000);
console.log(bubbleSort(nums));