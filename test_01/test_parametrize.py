import  pytest
class Test_Pytest:
    params=[1,2,3]
    params1=[4,5,6]
    @pytest.mark.parametrize("message1",params)
    @pytest.mark.parametrize("message2",params1)
    def test_one(self,message1,message2):

        print("执行test_one %d",message1 * message2)
        assert 1==1

    def test_two(self):
        print("执行test_two")
        assert 1==1

    def test_three(self):
        print("执行test_three")
        assert 1==1

if __name__ == '__main__':
    pytest.main(["-s","test_parametrize.py"])