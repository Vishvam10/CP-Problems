type MyQueue struct {
    st []int
    temp []int
}


func Constructor() MyQueue {
    st := []int{}
    temp := []int{}

    return MyQueue{st: st, temp: temp}
}


func (this *MyQueue) Push(x int)  {
    
    for len(this.st) > 0 {
        this.temp = append(this.temp, this.st[len(this.st)-1])
        this.st = this.st[:len(this.st)-1]
    }

    this.st = append(this.st, x)

    for len(this.temp) > 0 {
        this.st = append(this.st, this.temp[len(this.temp)-1])
        this.temp = this.temp[:len(this.temp)-1]
    }
}


func (this *MyQueue) Pop() int {
    val := this.st[len(this.st) - 1]
    this.st = this.st[:len(this.st) - 1]
    return val
}


func (this *MyQueue) Peek() int {
    val := this.st[len(this.st) - 1]
    return val
}


func (this *MyQueue) Empty() bool {
    return len(this.st) == 0
}


/**
 * Your MyQueue object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Push(x);
 * param_2 := obj.Pop();
 * param_3 := obj.Peek();
 * param_4 := obj.Empty();
 */
