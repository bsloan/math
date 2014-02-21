//
//  VecXd.h
//  warmup
//
//  Created by Brian Sloan on 2/1/14.
//  Copyright (c) 2014 Brian Sloan. All rights reserved.
//

#ifndef __VecXd_H__
#define __VecXd_H__

using namespace std;

template <class T>
class VecXd
{  
  public:
    VecXd<T>(); // constructor
   ~VecXd<T>(); // destructor
  
    VecXd<T>(const VecXd<T> &vec);  // copy constructor
    VecXd<T>(const VecXd<T> &&vec); // move constructor

    VecXd<T> &operator=(const VecXd<T> &vec);  // copy assignment
    VecXd<T> &operator=(const VecXd<T> &&vec); // move assignment
  
    VecXd<T> &operator+=(const VecXd<T> &vec);

    // overload input/output stream operators (not members)
    template <typename U>
    friend ostream &operator<<(ostream &out, VecXd<U> &vec);
    template <typename U>
    friend istream &operator>>(istream &in, VecXd<U> &vec);

  private:
    T *contents;
    int D;
};

// include the implementation to keep linker happy
#include "VecXd.cpp"

#endif
