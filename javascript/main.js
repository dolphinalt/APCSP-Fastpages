function binarySearch(v,To_Find)
{
    let lo = 0;
    let hi = v.length - 1;
    let mid;
     
    // This below check covers all cases , so need to check
    // for mid=lo-(hi-lo)/2
    while (hi - lo > 1) {
        console.log(lo)
        console.log(hi)
        let mid = (hi + lo) / 2;
        if (v[mid] < To_Find) {
            lo = mid + 1;
        }
        else {
            hi = mid;
        }
    }
    if (v[lo] == To_Find) {
        console.log( "Found At Index " + lo);
    }
    else if (v[hi] == To_Find) {
        console.log("Found At Index " + hi);
    }
    else {
        console.log("Not Found");
    }
}
const v = [2, 4, 6, 8, 11, 13, 15, 17, 19, 20, 21, 22, 23, 24, 25]
binarySearch(v, 15)