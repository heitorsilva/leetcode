require_relative './twosum'

describe 'Two Sum' do
  describe 'when two numbers in a list sums to a target' do
    it 'should return the indices of these two numbers' do
      numbers = [2,7,11,15]
      target = 9

      expect(two_sum(numbers, target)).to eq([0, 1])
    end
  end
end
